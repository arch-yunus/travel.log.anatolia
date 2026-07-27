import sys
import os

# Reconfigure stdout to use UTF-8 to prevent Unicode crashes on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from rich.align import Align
from rich.text import Text
import time
import os
import json
from datetime import datetime
from map_generator import MapGenerator
from analytics import TravelLogAnalytics
import random

console = Console()

class TravelCLI:
    def __init__(self):
        self.analytics = TravelLogAnalytics()
        self.map_gen = MapGenerator()

    def cinematic_boot(self):
        """Simulates a system boot / traveler's spiritual preparation."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        boot_text = Text("SİSTEM BAŞLATILIYOR... DİJİTAL SEYAHATNAME vPRO", style="bold green")
        console.print(Panel(boot_text, expand=False, border_style="green"))
        time.sleep(0.3)
        
        steps = [
            "Koordinatlar ve Veriler Yükleniyor...",
            "Tarihin İzleri Haritaya İşleniyor...",
            "Heybe ve Zihin Hazırlanıyor...",
            "Pusula Kalibre Ediliyor...",
            "Yeni Rota Hesaplanıyor..."
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task1 = progress.add_task("[cyan]Sistem ve Rota Hazırlığı", total=100)
            
            for step in steps:
                progress.update(task1, description=f"[cyan][BİLGİ] {step}")
                while progress.tasks[0].completed < progress.tasks[0].total:
                    time.sleep(0.01)
                    progress.update(task1, advance=random.randint(2, 5))
                    if random.random() < 0.1:
                        break
            
            while progress.tasks[0].completed < 100:
                time.sleep(0.01)
                progress.update(task1, advance=5)
                
        console.print("\n[bold green]SİSTEM HAZIR. İYİ YOLCULUKLAR.[/bold green]\n")
        time.sleep(0.2)

    def print_menu(self):
        menu_text = (
            "[bold cyan]1.[/bold cyan] 📝 Yeni Rota/Menzil Kaydet (New Entry)\n"
            "[bold cyan]2.[/bold cyan] 🗺️  Manevi Seyir Haritasını Çiz (Update Map)\n"
            "[bold cyan]3.[/bold cyan] 📊 Keşif Tablosu (Dashboard)\n"
            "[bold cyan]4.[/bold cyan] 🔍 Kayıtları ve Anıları Ara (Deep Search)\n"
            "[bold cyan]5.[/bold cyan] 💰 Bütçe & Tasarruf Analizi (Budget Calculator)\n"
            "[bold cyan]6.[/bold cyan] 📦 Veriyi Dışarı Aktar (Export)\n"
            "[bold cyan]7.[/bold cyan] ❌ Sistemi Kapat (Exit)\n"
        )
        
        panel = Panel(
            Align.center(menu_text),
            title="[bold magenta]DİJİTAL SEYAHATNAME vPRO[/bold magenta]",
            border_style="magenta",
            expand=False
        )
        console.print(panel)

    def create_entry(self):
        console.print("\n[bold cyan]>>> YENİ BİR MENZİL KAYDEDİLİYOR <<<[/bold cyan]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=4)
        table.add_column("İklim (Region)", style="bold blue")
        
        for idx, region in enumerate(self.analytics.REGIONS):
            table.add_row(str(idx+1), region)
            
        console.print(table)
        
        choice_input = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Bölge Numarası Seç")
        try:
            choice = int(choice_input)
            if 1 <= choice <= len(self.analytics.REGIONS):
                region = self.analytics.REGIONS[choice-1]
            else:
                 console.print("[bold red]>> GEÇERSİZ SEÇİM.[/bold red]")
                 return
        except ValueError:
             console.print("[bold red]>> GEÇERSİZ SEÇİM.[/bold red]")
             return

        city = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Hedef Şehir (örn. Konya)")
        location = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Ziyaret Edilen Mekan (örn. Hattuşaş)")
        
        region_path = os.path.join(".", region)
        city_path = os.path.join(region_path, city)
        loc_path = os.path.join(city_path, location.replace(" ", "_"))
        
        if os.path.exists(loc_path):
            console.print("[bold yellow]>> UYARI: Bu mekan zaten kaydedilmiş![/bold yellow]")
            if not Confirm.ask("Üzerine yazılsın mı?"):
                return

        os.makedirs(loc_path, exist_ok=True)
        
        coords = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Koordinatlar (Enlem, Boylam) [İsteğe Bağlı]", default="")
        quote = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Karalama Defterinden Kısacık Bir Not", default="")
        
        try:
            with open(os.path.join("_Sablon", "location_template.md"), "r", encoding="utf-8") as f:
                template_content = f.read()
        except FileNotFoundError:
            console.print("[bold red]>> CRITICAL ERROR: Template Missing![/bold red]")
            return

        filled_content = template_content.replace("[Lokasyon Adı]", location)
        filled_content = filled_content.replace("DD.MM.YYYY", datetime.now().strftime("%d.%m.%Y"))
        
        if coords:
            filled_content = filled_content.replace("XX.XXXX, YY.YYYY", coords)
        
        if quote:
            filled_content = filled_content.replace("[Buraya lokasyonla ilgili kısa, vurucu bir alıntı veya his eklenecek]", quote)
            
        target_file = os.path.join(loc_path, "README.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(filled_content)
            
        console.print(f"\n[bold green]>> KAYIT BAŞARILI:[bold green] Şuraya işlendi:\n{target_file}")
        time.sleep(1)

    def interactive_mode(self):
        self.cinematic_boot()
        while True:
            self.print_menu()
            choice = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Komut Nedir?")
            
            if choice == "1":
                self.create_entry()
            elif choice == "2":
                with console.status("[bold green]Seyir Haritası Çiziliyor...") as status:
                    try:
                        self.map_gen.generate_map()
                        console.print("[bold green]>> Harita oluşturuldu: travel_map.html.[/bold green]")
                    except Exception as e:
                        console.print(f"[bold red]>> Harita çizilirken hata oluştu: {e}[/bold red]")
                time.sleep(1)
            elif choice == "3":
                self.analytics.run_analysis()
                Prompt.ask("\n[bold yellow][MENÜYE DÖNMEK İÇİN ENTER'A BAS][/bold yellow]")
            elif choice == "4":
                keyword = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Aranacak Kelimeyi Girin")
                if not keyword:
                    continue
                
                console.print(f"\n[bold cyan]>>> Vadi ve tepelerde '{keyword}' izi sürülüyor... <<<[/bold cyan]")
                
                found_results = []
                for root, dirs, files in os.walk("."):
                    if "_Sablon" in root or ".git" in root or ".github" in root or "assets" in root:
                        continue
                    for file in files:
                        if file.endswith(".md"):
                            filepath = os.path.join(root, file)
                            try:
                                with open(filepath, "r", encoding="utf-8") as f:
                                    lines = f.readlines()
                                    for idx, line in enumerate(lines):
                                        if keyword.lower() in line.lower():
                                            snippet = line.strip()
                                            if len(snippet) > 60:
                                                snippet = snippet[:57] + "..."
                                            found_results.append((filepath, idx + 1, snippet))
                            except Exception as e:
                                pass
                
                if not found_results:
                    console.print("[bold yellow]>> UYARI: Bellekte herhangi bir iz bulunamadı.[/bold yellow]")
                else:
                    search_table = Table(show_header=True, header_style="bold magenta")
                    search_table.add_column("Dosya", style="dim", width=40)
                    search_table.add_column("Satır", justify="right", style="bold blue", width=6)
                    search_table.add_column("Cümle", style="italic cyan")
                    
                    for res in found_results:
                        # Clean filepath for display (remove ./)
                        disp_path = res[0].replace(".\\", "").replace("./", "")
                        search_table.add_row(disp_path, str(res[1]), res[2])
                    
                    console.print("\n")
                    console.print(search_table)
                    console.print(f"\n[bold green]>> Toplam {len(found_results)} eşleşme bulundu.[/bold green]")
                Prompt.ask("\n[bold yellow][MENÜYE DÖNMEK İÇİN ENTER'A BAS][/bold yellow]")

            elif choice == "5":
                self.run_budget_analysis()
            elif choice == "6":
                export_file = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                self.export_data_to_file(export_file)
                self.export_data_to_file("travel_data.json")
                time.sleep(1)
            elif choice == "7":
                console.print("[bold green]>> Sistem Kapatıldı. İyi yolculuklar.[/bold green]")
                break
            else:
                console.print("[bold red]>> GEÇERSİZ KOMUT.[/bold red]")
                time.sleep(0.5)

    def export_data_to_file(self, filename="travel_data.json"):
        console.print(f"[bold cyan]>> Seyahat verileri {filename} dosyasına derleniyor...[/bold cyan]")
        data = []
        regions = [
            "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
            "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
        ]
        for r in regions:
            if not os.path.exists(r):
                continue
            for city in os.listdir(r):
                city_path = os.path.join(r, city)
                if not os.path.isdir(city_path):
                    continue
                
                subdirs = [d for d in os.listdir(city_path) if os.path.isdir(os.path.join(city_path, d))]
                
                if not subdirs:
                    readme_path = os.path.join(city_path, "README.md")
                    if os.path.exists(readme_path):
                        data.append({
                            "region": city,
                            "city": "Unknown",
                            "location": "Unknown",
                            "path": readme_path.replace("/", "\\"),
                            "size_bytes": os.path.getsize(readme_path)
                        })
                else:
                    for s in subdirs:
                        readme_path = os.path.join(city_path, s, "README.md")
                        if os.path.exists(readme_path):
                            data.append({
                                "region": city,
                                "city": s,
                                "location": "Unknown",
                                "path": readme_path.replace("/", "\\"),
                                "size_bytes": os.path.getsize(readme_path)
                            })
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            console.print(f"[bold green]>> Veriler başarıyla aktarıldı: {filename}[/bold green]")
        except Exception as e:
            console.print(f"[bold red]>> Aktarım sırasında hata oluştu: {e}[/bold red]")

    def run_budget_analysis(self):
        console.print("\n[bold cyan]>>> BÜTÇE & TASARRUF HESAPLAYICI (vPRO) <<<[/bold cyan]")
        console.print("GSB Seyahatsever kapsamında KYK yurtlarında kalarak elde ettiğiniz konaklama tasarrufunu hesaplayın.\n")
        
        visited_cities = self.analytics.get_visited_cities()
        visited_count = len(visited_cities)
        
        if visited_count == 0:
            console.print("[bold yellow]>> UYARI: Henüz ziyaret edilmiş bir şehir bulunmuyor![/bold yellow]")
            Prompt.ask("\n[bold yellow][MENÜYE DÖNMEK İÇİN ENTER'A BAS][/bold yellow]")
            return

        hotel_input = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Ortalama Otel Gecelik Ücreti (TL)", default="1500")
        food_input = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Günlük Yemek Bütçesi (TL)", default="300")
        travel_input = Prompt.ask("[bold green]yolcu@seyahat:~[/bold green] Şehirlerarası Ortalama Ulaşım (TL)", default="500")
        
        try:
            hotel_rate = int(hotel_input)
            food_rate = int(food_input)
            travel_rate = int(travel_input)
        except ValueError:
            console.print("[bold red]>> GEÇERSİZ DEĞER. Sayısal değerler girmelisiniz.[/bold red]")
            time.sleep(1.5)
            return
            
        total_days = visited_count * 5
        savings = total_days * hotel_rate
        cost = (total_days * food_rate) + (visited_count * travel_rate)
        profit = savings - cost
        study_hours = total_days * 4
        
        table = Table(title="[bold green]Bütçe ve Tasarruf Sonuç Raporu[/bold green]", show_header=True, header_style="bold magenta")
        table.add_column("Parametre", style="cyan")
        table.add_column("Değer / Sonuç", justify="right", style="bold white")
        
        table.add_row("Ziyaret Edilen İl Sayısı", f"{visited_count} İl")
        table.add_row("Sahada Geçen Toplam Gün (5 Gün Kuralı)", f"{total_days} Gün")
        table.add_row("Kütüphane Çalışma / Upskilling Süresi", f"{study_hours} Saat")
        table.add_row("🏠 Toplam KYK Konaklama Tasarrufu", f"{savings:,} TL".replace(",", "."))
        table.add_row("🚌 Toplam Seyahat Maliyeti (Yemek+Yol)", f"{cost:,} TL".replace(",", "."))
        
        profit_color = "green" if profit >= 0 else "red"
        table.add_row("💡 Net Finansal Kazanç", f"[{profit_color}]{profit:,} TL[/{profit_color}]".replace(",", "."))
        
        console.print(table)
        Prompt.ask("\n[bold yellow][MENÜYE DÖNMEK İÇİN ENTER'A BAS][/bold yellow]")

    def main(self):
        parser = argparse.ArgumentParser(description="Seyahatname vPRO")
        subparsers = parser.add_subparsers(dest="command", help="System Commands")
        
        subparsers.add_parser("add", help="New Entry")
        subparsers.add_parser("map", help="Update Map")
        subparsers.add_parser("stats", help="Show Dashboard")
        subparsers.add_parser("export", help="Export travel data to JSON")
        
        args = parser.parse_args()
        
        if args.command == "add":
            self.create_entry()
        elif args.command == "map":
            self.map_gen.generate_map()
        elif args.command == "stats":
            self.analytics.run_analysis()
        elif args.command == "export":
            self.export_data_to_file("travel_data.json")
        else:
            self.interactive_mode()

if __name__ == "__main__":
    cli = TravelCLI()
    try:
        cli.main()
    except KeyboardInterrupt:
        console.print("\n[bold red]>> FORCED SHUTDOWN.[/bold red]")
