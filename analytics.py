import os
import sys
import time
import argparse
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
from rich.progress import track

# Reconfigure stdout to use UTF-8 to prevent Unicode crashes on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()

class TravelLogAnalytics:
    REGIONS = [
        "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
        "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
    ]

    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.stats = {
            "total_regions": 0,
            "total_cities": 0,
            "total_locations": 0,
        }

    def _normalize(self, name):
        tr_to_en = {
            'ı': 'i', 'I': 'I', 'İ': 'I', 'i': 'i',
            'ğ': 'g', 'Ğ': 'G',
            'ü': 'u', 'Ü': 'U',
            'ş': 's', 'Ş': 'S',
            'ö': 'o', 'Ö': 'O',
            'ç': 'c', 'Ç': 'C'
        }
        name = name.translate(str.maketrans(tr_to_en))
        return name.lower().strip()

    def get_visited_cities(self):
        visited = set()
        readme_path = os.path.join(self.root_dir, "README.md")
        if os.path.exists(readme_path):
            import re
            try:
                with open(readme_path, "r", encoding="utf-8") as f:
                    content = f.read()
                matches = re.findall(r"✅ \*\*([^\*]+)\*\*", content)
                for m in matches:
                    visited.add(self._normalize(m.strip()))
            except Exception:
                pass
        return visited

    def scan_region(self, region_name, visited_set=None):
        """Scans a single region directory."""
        if not os.path.exists(region_name):
            return None

        # Compatibility for tests: if no README exists, count all
        readme_path = os.path.join(self.root_dir, "README.md")
        if not os.path.exists(readme_path):
            is_visited = lambda c: True
        else:
            if visited_set is None:
                visited_set = self.get_visited_cities()
            is_visited = lambda c: self._normalize(c) in visited_set

        data = {"cities": 0, "locations": 0}
        try:
            for city in os.listdir(region_name):
                city_path = os.path.join(region_name, city)
                if os.path.isdir(city_path):
                    if is_visited(city):
                        data["cities"] += 1
                        location_count = 0
                        for loc in os.listdir(city_path):
                            loc_path = os.path.join(city_path, loc)
                            if os.path.isdir(loc_path):
                                location_count += 1
                        data["locations"] += location_count
        except Exception as e:
            # Silently handle unreadable or empty subdirectories
            pass
            
        return data

    def print_dashboard(self, region_data):
        """Prints a high-tech dashboard summary."""
        r_count = str(self.stats['total_regions'])
        c_count = str(self.stats['total_cities'])
        l_count = str(self.stats['total_locations'])
        
        dashboard_content = (
            r"[bold cyan]           _    ____  ____   ___  [/bold cyan]" + "\n"
            r"[bold cyan]     __  _| |_ |  _ \|  _ \ / _ \ [/bold cyan]" + "\n"
            r"[bold cyan]     \ \/ /   \| |_) | |_) | | | |[/bold cyan]" + "\n"
            r"[bold cyan]      \  /| |_) |  __/|  _ <| |_| |[/bold cyan]" + "\n"
            r"[bold cyan]       \/ |____/|_|   |_| \_\\___/ [/bold cyan]" + "\n\n"
            f"[cyan]REGIONS:[/cyan] [bold white]{r_count}[/bold white] │ "
            f"[cyan]CITIES:[/cyan] [bold white]{c_count}[/bold white] │ "
            f"[green]LOCATIONS:[/green] [bold white]{l_count}[/bold white]\n"
        )
        
        if region_data:
            best_region = max(region_data, key=lambda x: x[1])
            dashboard_content += f"\n[bold yellow]🔥 HOTSPOT:[/bold yellow] {best_region[0]} ({best_region[1]} Locs)"
            
        console.print(Panel(Align.center(dashboard_content), title="[bold magenta]MISSION STATUS REPORT[/bold magenta]", border_style="magenta", expand=False))

    def run_analysis(self, mock_delay=False):
        """Main analysis loop using Rich."""
        
        if not mock_delay:
            os.system('cls' if os.name == 'nt' else 'clear')
        
        header = """[bold cyan]
    ╔══════════════════════════════════════════════════════════════╗
    ║   TRAVEL LOG ANALYTICS CORE vPRO                             ║
    ║   CONNECTED TO: ANADOLU_DATABASE                             ║
    ╚══════════════════════════════════════════════════════════════╝
        [/bold cyan]"""
        console.print(header)
        
        if not mock_delay:
            with console.status("[bold green]Uplinking to Satellite Network...") as status:
                time.sleep(1)
                status.update("[bold green]Downloading Manifest...")
                time.sleep(1)
        
        table = Table(title="[bold blue]Region Data Analysis[/bold blue]", show_header=True, header_style="bold magenta")
        table.add_column("REGION ID", style="cyan", width=25)
        table.add_column("CITIES", justify="right", style="green")
        table.add_column("LOCATIONS", justify="right", style="yellow")
        
        region_data = []

        visited_set = self.get_visited_cities()
        self.stats = {
            "total_regions": 0,
            "total_cities": 0,
            "total_locations": 0,
        }

        for region in self.REGIONS:
            result = self.scan_region(region, visited_set=visited_set)
            
            region_cities = 0
            region_locations = 0
            
            if result:
                self.stats["total_regions"] += 1
                region_cities = result["cities"]
                region_locations = result["locations"]
                self.stats["total_cities"] += region_cities
                self.stats["total_locations"] += region_locations
            
            region_data.append((region, region_locations))

            if not mock_delay: time.sleep(0.1)
            
            table.add_row(region, str(region_cities), str(region_locations))

        console.print(table)
        
        # Graph Section with Block Characters using Rich
        console.print("\n[bold]>>> DENSITY VISUALIZATION <<<[/bold]")
        
        chart_table = Table.grid(padding=1)
        chart_table.add_column(style="cyan", justify="right")
        chart_table.add_column()
        chart_table.add_column(style="bold white")
        
        if region_data:
            max_loc = max([x[1] for x in region_data])
            max_loc = max_loc if max_loc > 0 else 1
            for region, count in region_data:
                bar_len = int((count / max_loc) * 30)
                bar = "[green]" + "▓" * bar_len + "[/green]" + "[dim]" + "░" * (30 - bar_len) + "[/dim]"
                chart_table.add_row(region, bar, str(count))
                
        console.print(Panel(chart_table, border_style="cyan"))

        self.print_dashboard(region_data)

        if not mock_delay:
            console.print("\n[bold cyan]> SESSION TERMINATED.[/bold cyan]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Travel Log Analytics Tool vPRO")
    parser.add_argument("--fast", action="store_true", help="Skip animations")
    args = parser.parse_args()

    analytics = TravelLogAnalytics()
    try:
        analytics.run_analysis(mock_delay=args.fast)
    except KeyboardInterrupt:
        console.print("\n[bold red]> ABORTED.[/bold red]")
