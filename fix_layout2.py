import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The user is complaining that "Müşterilerimiz Neler Söylüyor?" section is duplicated or misplaced.
# Currently, the REAL reviews are in <section id="hizmetler"> and the FAKE reviews are in <section id="referanslar">.

# 1. Extract the REAL reviews from #hizmetler
hizmetler_pattern = re.compile(r'(<section class="py-16 bg-surface-container-lowest w-full" id="hizmetler">.*?)(<div class="flex flex-wrap justify-center gap-6">.*?)(?=\s*<!-- Bottom Row \()', re.DOTALL)
match = hizmetler_pattern.search(content)

if match:
    real_reviews_html = match.group(2).strip()
    
    # 2. Restore the original Hizmetler cards
    original_hizmetler = """<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Card 1 -->
            <div class="bg-white rounded-[28px] p-4 shadow-sm border border-surface-container-low flex flex-col group cursor-pointer hover:shadow-md transition-all duration-300 hover:scale-[1.02]">
                <div class="w-full h-56 md:h-64 rounded-[20px] overflow-hidden mb-5 relative">
                    <img src="images/kurulum.jpeg" alt="Klima Kurulumu" class="w-full h-full object-cover">
                </div>
                <div class="px-4 pb-4 flex flex-col flex-grow">
                    <h3 class="text-4xl md:text-5xl font-headline-md font-bold text-on-surface mb-3">Klima Kurulumu</h3>
                    <p class="text-on-surface-variant mb-6 text-base flex-grow">Uzman ekibimizle yeni nesil cihazların profesyonel ve temiz kurulumu.</p>
                    <div class="flex items-center text-[#4A1D96] font-bold gap-1 text-base">
                        <span>İncele</span>
                        <span class="material-symbols-outlined text-lg group-hover:translate-x-1 transition-transform">arrow_forward</span>
                    </div>
                </div>
            </div>
            
            <!-- Card 2 -->
            <div class="bg-white rounded-[28px] p-4 shadow-sm border border-surface-container-low flex flex-col group cursor-pointer hover:shadow-md transition-all duration-300 hover:scale-[1.02]">
                <div class="w-full h-56 md:h-64 rounded-[20px] overflow-hidden mb-5 relative">
                    <img src="images/isitma.jpeg" alt="Isıtma Sistemleri" class="w-full h-full object-cover">
                </div>
                <div class="px-4 pb-4 flex flex-col flex-grow">
                    <h3 class="text-4xl md:text-5xl font-headline-md font-bold text-on-surface mb-3">Isıtma Sistemleri</h3>
                    <p class="text-on-surface-variant mb-6 text-base flex-grow">Kış aylarında sıcak ve konforlu ortamlar için yüksek verimli ısı pompaları.</p>
                    <div class="flex items-center text-[#4A1D96] font-bold gap-1 text-base">
                        <span>İncele</span>
                        <span class="material-symbols-outlined text-lg group-hover:translate-x-1 transition-transform">arrow_forward</span>
                    </div>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="bg-white rounded-[28px] p-4 shadow-sm border border-surface-container-low flex flex-col group cursor-pointer hover:shadow-md transition-all duration-300 hover:scale-[1.02]">
                <div class="w-full h-56 md:h-64 rounded-[20px] overflow-hidden mb-5 relative">
                    <img src="images/bakim.jpeg" alt="Bakım Planları" class="w-full h-full object-cover">
                </div>
                <div class="px-4 pb-4 flex flex-col flex-grow">
                    <h3 class="text-4xl md:text-5xl font-headline-md font-bold text-on-surface mb-3">Bakım Planları</h3>
                    <p class="text-on-surface-variant mb-6 text-base flex-grow">Düzenli periyodik bakımlarla cihazınızın ömrünü uzatın ve enerjiden tasarruf edin.</p>
                    <div class="flex items-center text-[#4A1D96] font-bold gap-1 text-base">
                        <span>İncele</span>
                        <span class="material-symbols-outlined text-lg group-hover:translate-x-1 transition-transform">arrow_forward</span>
                    </div>
                </div>
            </div>
        </div>"""
        
    content = content[:match.start(2)] + original_hizmetler + '\n        ' + content[match.end(2):]
    
    # 3. Replace the old reviews in #referanslar with the real reviews
    ref_pattern = re.compile(r'(<section class="py-16 bg-surface-container-lowest w-full" id="referanslar">.*?<div class="max-w-7xl mx-auto px-4 md:px-8 flex flex-col gap-12">.*?)(<div class="grid grid-cols-1 md:grid-cols-3 gap-6">.*?)(?=    </div>\n</section>)', re.DOTALL)
    
    ref_match = ref_pattern.search(content)
    if ref_match:
        content = content[:ref_match.start(2)] + real_reviews_html + '\n' + content[ref_match.end(2):]
        print("Layout completely fixed!")
    else:
        print("Referanslar section pattern not found!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Hizmetler pattern not found!")
