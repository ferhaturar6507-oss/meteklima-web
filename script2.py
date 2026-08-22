import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace brand name
content = content.replace('Esinti Klima', 'Mete Klima')
content = content.replace('Esinti', 'Mete')

# 2. Update the Footer to include the real address and phone
footer_old = '''© 2024 Mete Klima. Antalya'nın Serin Nefesi.'''
footer_new = '''© 2024 Mete Klima. Antalya'nın Serin Nefesi.<br>
                Merkez, 2130. Sk. no: 6/1, 07500 Serik/Antalya<br>
                <span class="font-bold">7/24 Açık</span> | <span class="font-bold">0507 032 56 40</span>'''
content = content.replace(footer_old, footer_new)

# 3. New Reviews HTML
reviews_html = """
        <div class="flex flex-wrap justify-center gap-6">
            <!-- Review 1 -->
            <div class="w-full md:w-[calc(33.333%-16px)] bg-surface-container-low rounded-2xl p-8 flex flex-col gap-6 shadow-sm border border-surface-container hover:shadow-md transition-shadow">
                <div class="flex text-[#FFB400] gap-1">
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
                <blockquote class="text-body-lg font-body-lg text-on-surface italic flex-grow">
                    "Tek kelimeyle kalitenin adresi Mete beye teşekkür ederim işçiliği temiz ve güzeldi kesinlikle tavsiye ederim."
                </blockquote>
                <div class="flex items-center gap-4 pt-6 border-t border-outline-variant/30 mt-auto">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">SŞ</div>
                    <div class="flex flex-col">
                        <span class="text-body-md font-bold text-on-surface">Selçuk Şahin</span>
                        <span class="text-sm text-on-surface-variant">1 Yıl Önce</span>
                    </div>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="w-full md:w-[calc(33.333%-16px)] bg-surface-container-low rounded-2xl p-8 flex flex-col gap-6 shadow-sm border border-surface-container hover:shadow-md transition-shadow">
                <div class="flex text-[#FFB400] gap-1">
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
                <blockquote class="text-body-lg font-body-lg text-on-surface italic flex-grow">
                    "Klima bakım ve montaj yaptırdım işçilik güzel ve temiz yaptı herkese tavsiye ederim"
                </blockquote>
                <div class="flex items-center gap-4 pt-6 border-t border-outline-variant/30 mt-auto">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">CT</div>
                    <div class="flex flex-col">
                        <span class="text-body-md font-bold text-on-surface">coşkun taş</span>
                        <span class="text-sm text-on-surface-variant">1 Yıl Önce</span>
                    </div>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="w-full md:w-[calc(33.333%-16px)] bg-surface-container-low rounded-2xl p-8 flex flex-col gap-6 shadow-sm border border-surface-container hover:shadow-md transition-shadow">
                <div class="flex text-[#FFB400] gap-1">
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
                <blockquote class="text-body-lg font-body-lg text-on-surface italic flex-grow">
                    "Mükemmel müşteri memnuniyeti , Temiz işçilik , kalitenin adresi herkese tavsiye ederim 👍"
                </blockquote>
                <div class="flex items-center gap-4 pt-6 border-t border-outline-variant/30 mt-auto">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">EA</div>
                    <div class="flex flex-col">
                        <span class="text-body-md font-bold text-on-surface">Erhan Altınay</span>
                        <span class="text-sm text-on-surface-variant">1 Yıl Önce</span>
                    </div>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="w-full md:w-[calc(33.333%-16px)] bg-surface-container-low rounded-2xl p-8 flex flex-col gap-6 shadow-sm border border-surface-container hover:shadow-md transition-shadow">
                <div class="flex text-[#FFB400] gap-1">
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
                <blockquote class="text-body-lg font-body-lg text-on-surface italic flex-grow">
                    "Klima temizliği ve yer değişimi yaptırdım çok pratik ve çabuk halledildi çok temiz çalıştı çok memnun kaldım"
                </blockquote>
                <div class="flex items-center gap-4 pt-6 border-t border-outline-variant/30 mt-auto">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">ET</div>
                    <div class="flex flex-col">
                        <span class="text-body-md font-bold text-on-surface">Elif Tavlar</span>
                        <span class="text-sm text-on-surface-variant">1 Yıl Önce</span>
                    </div>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="w-full md:w-[calc(33.333%-16px)] bg-surface-container-low rounded-2xl p-8 flex flex-col gap-6 shadow-sm border border-surface-container hover:shadow-md transition-shadow">
                <div class="flex text-[#FFB400] gap-1">
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
                <blockquote class="text-body-lg font-body-lg text-on-surface italic flex-grow">
                    "Klimamın bakımlarını yaptı temizledi ısıtma soğutmada sorun yaşıyordum mete klima sayesinde sorunlarım giderildi teşekkür ederim tavsiye ederim herkese"
                </blockquote>
                <div class="flex items-center gap-4 pt-6 border-t border-outline-variant/30 mt-auto">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">AK</div>
                    <div class="flex flex-col">
                        <span class="text-body-md font-bold text-on-surface">ABDULLAH Kılınç</span>
                        <span class="text-sm text-on-surface-variant">1 Yıl Önce</span>
                    </div>
                </div>
            </div>
        </div>
"""

# Replace the old reviews grid with the new reviews flex-wrap layout
start_str = '<div class="grid grid-cols-1 md:grid-cols-3 gap-6">'
end_str = '</div>\n    </div>\n</section>\n<!-- 7. SSS Section -->' # We need to be careful with end_str.
# Wait, let's use regex to replace the grid completely inside the #referanslar section

pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">.*?</div>\n    </div>\n</section>', re.DOTALL)
match = pattern.search(content)

if match:
    content = content[:match.start()] + reviews_html + '\n    </div>\n</section>' + content[match.end():]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
