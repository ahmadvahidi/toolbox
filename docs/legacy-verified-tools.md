# ابزارهای تأییدشده (Verified Tools)

منبع: فورواردهای تبلیغاتی که احمد می‌فرستد + بررسی گابیمارو.
قاعده: **هیچ ادعایی بدون بررسی باور نمی‌شود.** هر مدخل = چیستی، قیمت، محدودیت، لینک، تاریخ بررسی.

آخرین به‌روزرسانی: ۳ نوامبر ۲۰۲۶

---

## 🔥 FreeVideo + MiniMax H3 — GitHub: `FlashML-org/FreeVideo` (مهم‌ترین مورد برای ما)

- **چیستی:** موتور اجرای **محلی** مدل ویدیوی **MiniMax H3** روی GPU خانگی. Apache-2.0، پایتون، ~۱٫۸ هزار ستاره، نسخهٔ v0.4.0 (۱۳ اکتبر ۲۰۲۶ — فعال).
- **مزیت اصلی:** ساخت ویدیو با AI **رایگان و بی‌توکن** روی کامپیوتر خودت — بدون Gemini/Veo/اشتراک. مبنا: OpenVDN → مدل ۸ مرحله‌ای VDN-H3 + Video DeltaNet.
- **نیازمندی سخت‌افزار:** حداقل **8GB VRAM + 16GB RAM** (مسیر FreeVideo/VDN). مسیر معمول ComfyUI: خروجی بهینه‌شده ۴۲٫۵GB (از ۱۲۳٫۶GB) و توصیهٔ RTX 3060–4090. تست واقعی: RTX 3060 12GB → ویدیوی ۵ ثانیه‌ای 864×480 با Turbo 8-step ≈ **۴٫۵ دقیقه**.
- **مدل MiniMax H3:** وزن‌ها ۳ اوت ۲۰۲۶ متن‌باز شد (H3-Base، ۳۳٫۱B، ویدیو ۷۶۸p + صدای استریو). نسخهٔ **۲K** (H3-Regenerate-2K) متن‌باز **نیست** → فقط با API میزبانی‌شده.
- ⚠️ **لایسنس (متن رسمی، بازخوانی ۲۴ اکتبر ۲۰۲۶):** MiniMax H3 Community License — «Applicable Territory = worldwide, **excluding the European Union**, the United Kingdom, South Korea and the USA». یعنی استفاده از وزن‌ها **در آلمان مجاز نیست** (کل اتحادیهٔ اروپا مستثناست). «اوپن‌سورس» هم دقیقاً غلط است: open-weights با لایسنس اختصاصی، نه مجوز OSI.
- 🏆 **کیفیت (Artificial Analysis، آگوست–سپتامبر ۲۰۲۶):** در رأی کورکاربران، text-to-video با صدا H3 ≈ ۱۲۳۸ در برابر Veo 3.1 ≈ ۱۰۹۲–۱۰۹۵ (رتبهٔ ۱۱–۱۳)؛ image-to-video رتبهٔ ۱ تا ۳؛ ویرایش ویدیو رتبهٔ **۱** (Veo اصلاً روی این برد نیست). ولی در جدول کلی رتبهٔ **۸** است (۱۴۶۰ در برابر صدر ۱۵۱۶) → «بهترین مدل دنیا» نه، «بهترین مدل open-weights» بله.
- ✅ قابلیت‌ها: ComfyUI · LoRA · مک (Apple Silicon، پیش‌نمایش) · نصب لینوکس/ویندوز (`setup.sh` / `setup.cmd`).
- ❌ **سرور ما GPU ندارد** (۲ هسته + ~۸GB RAM) → اینجا اجرا نمی‌شود. یعنی: **این همان چیزی است که با خرید سرور GPU محقق می‌شود.**
- 📌 ریل فرستاده‌شده از پیج «آکادمی وب‌مسترمنتور» با طعمهٔ «کامنت بزن تا لینک دایرکت شود» (۵۱۳۹ کامنت) بود؛ اطلاعاتش درست است ولی برای جمع‌آوری لید است — نیازی به کامنت‌دادن نیست.

---

## 🎨 Isometric — isometric.buildlab.in (کامپوننت‌های ایزومتریک برای React)

- **چیستی:** کتابخانهٔ متن‌باز کامپوننت‌های **React + Tailwind** با طراحی خطی‑ایزومتریک (خط‌های نازک با عمق). نصب با shadcn CLI: `npx shadcn@latest add @isometric/all` — کد داخل پروژه کپی می‌شود (قفل فروشنده ندارد). روی **Radix** بنا شده، پس کیبورد و screen-reader درست کار می‌کند.
- **۴۱ کامپوننت (رجیستری تأییدشده در ۱۳ اکتبر ۲۰۲۶):**
  - **اشیای تعاملی:** PC Case · Heart · Pulley · Church · Reactor
  - **دنیای بلوکی (مثل ماینکرفت):** Block · Chest · Torch · Tree · Hotbar · Inventory · Hearts-meter · XP-bar · World
  - **فیگورها:** Skyline · Stack · Keys · Rack · Laptop · Bars · Steps · Files · Cylinders · Parcel · Nodes · Cube
  - **پریمیتیوهای UI:** Iso Button · Card · Switch · Tabs · Slider · Toggle Group · Kbd · Badge · Progress · Input · Grid + موتور `iso-depth`
- **وضعیت واقعی (کوچک و نو):** ریپو در ۴ اکتبر ۲۰۲۶ ساخته شده · **۶ ستاره** · صفر فورک · نسخهٔ v0.2 · سازنده: Abhishek Mallick (استودیوی BuildLab هند). سایت می‌گوید MIT، ولی گیت‌هاب لایسنس را `NOASSERTION` نشان می‌دهد.
- **پیش‌نمایش:** `previews/isometric-ui.png` (اسکرین‌شات واقعی صفحهٔ اصلی)
- ✅ **یاد گرفته و تست شد (۱۳ اکتبر ۲۰۲۶):** پروژهٔ نمونهٔ کارکننده در `/opt/data/workspace/isometric-demo` (Vite + React 19 + Tailwind v4، هر ۴۱ کامپوننت، `setup.sh` / `build.sh` / `serve.sh`). اسکرین‌شات‌های خودمان: `previews/iso-demo-a.png`, `-b.png`, `-c.png`. دانش فنی به‌صورت مهارت `isometric-ui` ذخیره شد.
- **نکتهٔ فنی مهم:** `src/lib/utils.ts` را از پکیج `cn` می‌سازد (جایگزین رسمی clsx+tailwind-merge از خود shadcn — سالم است).
- **کاربرد برای ما:** خوب برای صفحهٔ محصول/SaaS، لندینگ تکنیکال و پورتفولیو — یعنی اگر برای آموزش آلمانی یا برند ایمان سایت بسازیم. ❌ برای برند DOPEAK (دارک/انیمه) یا اسناد رسمی مناسب نیست؛ سبکش زمین تا آسمان فرق دارد.

---

## ✅ Duck.ai — duck.ai (DuckDuckGo)

- **رایگان، بدون حساب کاربری، بدون کارت بانکی.** چت‌ها ناشناس می‌شوند و روی داده‌هایت آموزش نمی‌بیند.
- **مدل‌های رایگان (تأییدشده در خودِ انتخاب‌کنندهٔ مدل، ۱۲ اکتبر ۲۰۲۶):** GPT-6 Luna · Claude 4.5 Haiku · Mistral Small 4 · GPT-5.4 nano · GPT-5.4 mini · gpt-oss-120b · Gemma 4 31B.
  پلن Plus: GPT-5.4 + Claude Sonnet 4.6 · پلن Pro: Claude Opus 4.8.
- **قابلیت‌ها:** New Image (ساخت و ویرایش تصویر) · New Voice Chat (مکالمهٔ صوتی) · Dictate (دیکته).
- ⚠️ **محدودیت مهم:** سقف مصرف **روزانه** دارد؛ «نامحدود» غلط است. روی VPN/سیم‌کارت/IP سرور ممکن است همان اول ارور بدهد (`Duck.ai is temporarily unavailable`).
- نکتهٔ وابسته: از ۷ اکتبر ۲۰۲۶ **GPT-6 Luna** مدل پلن رایگانِ خود ChatGPT هم هست (پلن‌های پولی: GPT-6 Sol).
- ✅ برای احمد: روی موبایل خوب کار می‌کند؛ برای تمرین آلمانی و سؤال سریع.

## ✅ Google AI Edge Gallery — اندروید / iOS

- رایگان، آفلاین، ۱۰۰٪ روی دستگاه. بدون ارسال داده به سرور.
- چت با **Gemma 4** (+ Thinking Mode) · Ask Image (تشخیص تصویر) · Audio Scribe (رونویسی و ترجمه) · **Instant Media Search** و **Video Moments Finder** (دموی EmbeddingGemma 2) · بنچمارک و مدیریت مدل.
- متن‌باز: `github.com/google-ai-edge/gallery`
- ✅ روی گوشی احمد قابل استفاده است.

## ⚠️ Google AI Edge Foresight — فقط مک با Apple Silicon

- رایگان و آزمایشی، تمام‌محلی و آفلاین: رونویسی زندهٔ صدای سیستم در جلسات (Meet/Zoom/حضوری)، تبدیل یادداشت‌های کوتاه به یادداشت کامل، سؤال‌وجواب زنده، سرچ در فایل‌ها/دیاگرام‌ها/تقویم (+ Google Drive).
- مدل‌ها: **EmbeddingGemma 2 + Gemma 4**. دانلود: `dl.google.com/foresight-mac/foresight_mac.dmg`
- ❌ نسخهٔ ویندوز/لینوکس/اندروید ندارد → روی گوشی احمد و روی سرور ما اجرا نمی‌شود.

## ✅ EmbeddingGemma 2 + Gemma 4 — مدل‌های متن‌باز گوگل

- **EmbeddingGemma 2:** ۷۴۰M پارامتر، open weights، چندوجهی (متن/کد/تصویر/ویدیو/صدا) در یک فضای برداری، ۷۶۸ بُعد، Matryoshka. انتشار: ۶ اکتبر ۲۰۲۶.
- **Gemma 4:** مدل چت/نوشتن روی دستگاه.
- در دسترس از HuggingFace / Kaggle؛ سازگار با llama.cpp، Ollama، Transformers، MLX، MediaPipe، LiteRT.
- کاربرد برای ما: **سرچ معنایی و RAG روی فایل‌های پروژه‌ها، کاملاً محلی و بدون ابر** (بدون هزینهٔ توکن).

## ⚠️ ArtCraft / Crafting Apps — getartcraft.com

- **واقعی است.** پروژهٔ متن‌باز (GitHub: `storytold`، سازنده Brandon Thomas / @echelon): بازنویسی ۱۲ برنامه با **Rust** — PhotoCraft، VectorCraft، FilmCraft، LightCraft، EffectCraft، DesignCraft، PdfCraft، WordCraft، GridCraft، DeckCraft، CADCraft، SoundCraft.
- رایگان، لایسنس MIT/Apache-2.0، نیتیو mac/Windows/Linux + نسخهٔ وب. Launcher نصب/به‌روزرسانی می‌کند (امضا + چک SHA-256، نصب از GitHub releases).
- **وضعیت واقعی (هایپ دارد):** نسخه‌ها ۰.۵–۰.۹ و چند روزه. **قابل استفاده: VectorCraft، EffectCraft، DesignCraft.** **خراب: PhotoCraft، FilmCraft** (کندی، مکان‌نمای متن، شورتکات‌های ازکارافتاده). PhotoCraft تنها ~۵۴ هزار ستاره دارد.
- ❌ سرور ما **headless** است → این اپ‌های گرافیکی اینجا اجرا نمی‌شوند؛ روی گوشی هم نه (فقط کامپیوتر).

---

## 🎮 OpenWhip — github.com/GitFrog1111/OpenWhip

- **چیستی:** اپ طنزِ Electron روی ترِی دسکتاپ — با کلیک، شلاق روی صفحه ظاهر می‌شود و وقتی می‌زنی، **Ctrl-C (interrupt)** به ترمینال Claude Code می‌فرستد + یکی از ۵ صدای تشویقی. (Win/mac آماده؛ لینوکس `xdotool` لازم دارد.)
- **وضعیت:** واقعی · MIT · ~۳٫۷ هزار ستاره · `npm install -g openwhip` (v1.1.0، ~۱۸۰۰ دانلود در ماه، منتشر آوریل ۲۰۲۶، آخرین کامیت مه ۲۰۲۶ — از آن وقت راکد).
- **✅ بررسی امنیتی (۱۲ اکتبر ۲۰۲۶):** بستهٔ npm تمیز است — بدون `postinstall`/`preinstall`، بدون هیچ درخواست شبکه یا ارسال داده، کد خوانا (`main.js`/`preload.js`). فقط `child_process` برای Alt+Tab و فرستادن Ctrl+C (ویندوز: koffi/user32 · مک: osascript · لینوکس: xdotool).
- ⚠️ در README یک **توکن مم‌کوین** تبلیغ شده (آدرس pump.fun) — به آن دست نزن؛ هیچ ربطی به کد ابزار ندارد.
- ❌ روی سرور ما اجرا نمی‌شود (headless، بدون میزکار/ترِی) و کاربرد جدی هم ندارد: فقط نشست Claude Code را قطع می‌کند.

---

## ✅ Hermes Bot Mode — «تیم ربات‌های هوش مصنوعی» (مستندات رسمی Hermes + ویدیوی پٍدی)

- **واقعی است.** فیچر رسمی خود Hermes به اسم **Bot Mode**: هر Bot = یک **پروفایل Hermes** جداگانه — مدل، حافظه، مهارت‌ها، شخصیت (SOUL.md)، چتِ اختصاصی و دائمی «Bot Chat»، و روتین‌های cron خودش. رابطش تبِ Bots در **دسکتاپ اپ** است و پیش‌فرض روشن است.
- ویدیو: «یک تیم ساختم که کارمنداش هوش مصنوعی‌ان! | آموزش Hermes Bots» — کانال **Pedi | پٍدی** (۸۱۲ سابسکرایبر)، منتشر ۱۲ اکتبر ۲۰۲۶، ۲۴ دقیقه، ۲٬۵۱۵ بازدید → `youtu.be/x4MbgIN1XO4`. محتوایش درست است (من به‌جای اعتماد به ویدیو، از **مستندات رسمی + کد نصب‌شده** تأیید کردم).
- ✅ **خودم روی همین سرور تستش کردم (۱۴ اکتبر ۲۰۲۶):** دو بات ساختم (`researcher` و `writer`)، Bot Chat آن‌ها را ساختم و یک پیام `message_agent` از اولی به دومی فرستادم — در دیتابیس پروفایل گیرنده با امضای «Message from 🤖 Researcher (@researcher)» ثبت شد. یعنی **بدون دسکتاپ، headless هم کار می‌کند** (روش کامل در مهارت `hermes-agent` → `references/bot-mode-headless.md`).
- ⚠️ محدودیت‌ها: roster گرافیکی، گروه‌چت چندباتی (room) و آواتار AI فقط در دسکتاپ اپ هستند و معادل CLI ندارند. برای رسیدن بات‌ها به تلگرام، هر پروفایل باید توکن بات خودش را بگیرد (`gateway.multiplex_profiles` روی این سرور فعال است).
- 💰 هزینه: `profile create --clone` کل مهارت‌ها را کپی می‌کند (**۷۲۳MB برای هر بات** روی این نصب) و هر تورنِ بات یک تورن کامل ایجنت است. برای بات‌های سبک `--no-skills`.

---

## 🔍 NullVPN — github.com/snarefps/NullVPN (واقعی، ولی بسته)

- **چیستی:** کلاینت چندسکویی Flutter برای کانفیگهای Xray (VLESS+REALITY/VMess/Trojan/Shadowsocks) + تونل رایگان WARP. رایگان، بدون تبلیغ/اکانت/تحلیل. v1.6.0 در ۱۳ اکتبر ۲۰۲۶.
- **هستههای بستهبندیشده (خودم از داخل tar.gz باز کردم):** `bin/xray` = **Xray 26.10.9** (۳۸MB، با LICENSE) · `bin/zeptun` = tun2socks در Zig (۵۷۳KB) · `bin/aether` = کلاینت Rust برای WARP/MASQUE (۲۱MB) · `bin/pt/lyrebird` (obfs4) · `bin/pt/psiphon-tunnel-core` · geoip.dat/geosite.dat.
- ✅ **تست واقعی (۱۸ اکتبر ۲۰۲۶):** `./bin/aether --wg --bind 127.0.0.1:1819` روی سرور headless در **۱۸ ثانیه** تونل ساخت: `ip=104.28.197.9 colo=FRA loc=DE warp=on` و SOCKS5 روی 1819. گزینهٔ `--exit-loc DE` برای انتخاب کشور خروجی وجود دارد → جایگزین بهتری برای ترفند wireproxy فعلی.
- ⚠️ **بسته است:** لایسنس proprietary freeware («All rights reserved») و مخزن گیتهاب **هیچ کد منبعی ندارد** (فقط README/LOGO/اسکرینشات). = اعتماد به یک توسعهدهندهٔ ناشناس (۱۰ ستاره، ۱ ماه).
- ⚠️ «همهٔ سیستمعاملها» نیمهدرست: v1.6.0 فقط اندروید (۳ ABI) + iOS (IPA امضانشده) + لینوکس (deb/rpm/AppImage/tar.gz) دارد؛ **ویندوز فقط در v1.2.0** و **فایل مک در آخرین نسخه نیست** (لینک README ۴۰۴). ویندوز/مک امضانشده.
- **پیشنیاز اصلی:** یا کانفیگ/سابسکریپشن خودت (لینک یا QR) — یا حالت **Aether** که بدون هیچ سرور/اکانتی از Cloudflare WARP تونل میسازد.

---

## 📱 whatsapp-mcp — github.com/finereli/whatsapp-mcp (echt, read-only)

- **Was:** MCP-Server, der die eigenen WhatsApp-Chats lesbar macht (suchen/lesen, nicht senden). MIT, TypeScript, ~260★ nach 1 Tag; läuft als Cloudflare Worker (Durable Object + SQLite/FTS5).
- **Getestet (19.10.2026):** Repo geklont, `local-export` installiert (Node v26.7.0, 50 MB deps) und gestartet → erreicht die QR-Stufe („Scan with WhatsApp"), QR wird im Terminal gerendert. Pairing selbst braucht das Handy des Besitzers.
- **Kosten:** Originalweg braucht **Workers Paid** (~$5/Monat) wegen `cpu_ms=300000` beim ersten Import; der `local-export`-Weg ist kostenlos (Snapshot als JSON pro Chat).
- **Risiken:** inoffiziell (Baileys) → gegen WhatsApp-AGB, geringes Sperrrisiko; keine Medien (nur `[image]`/`[voice note 12s]`); pro Deployment ein Konto.
- **Hermes-Anbindung:** `hermes mcp add --transport http whatsapp https://<url>/mcp` (Hermes hat vollen MCP-Client: add/list/test/login).
- Details: Skill `whatsapp-mcp`.

---

## 🚫 NovaDroid — github.com/rV9Cy/NovaDroid (دست نزن)

- **چیستی:** فورک فارسی‌شده و تغییرنام‌دادهٔ **PhoneSploit Pro** (۶٫۳ هزار ستاره، GPL-3.0، «all-in-one hacking tool to remotely take over Android devices») — با ADB + scrcpy + Nmap + Metasploit: استخراج SMS/مخاطبین/تماس‌ها/گالری، استریم دوربین و میکروفون، مدیریت اپ‌ها، و **زنجیرهٔ خودکار Metasploit** (ساخت payload با msfvenom → نصب → اجرا → نشست meterpreter = تصرف کامل دستگاه).
- **وضعیت فورک:** ساخته ۱۴ سپتامبر ۲۰۲۶ · **۵ ستاره** · همان روز رها شده.
- ⚖️ **قانونی (آلمان):** روی گوشی خودت یا دستگاهی که **مجوز کتبی** داری = تست نفوذ قانونی. روی گوشی هر کس دیگر = **جرم**: §202a StGB (Ausspähen von Daten) · §202b (Abfangen) · **§202c (صرفاً تهیه یا نگهداری این ابزار هم می‌تواند مجازات داشته باشد)** · §303a Datenveränderung. جملهٔ «educational use only» هیچ ارزش قانونی ندارد.
- 🦠 **ریسک امنیتی:** فورک ناشناس از یک ابزار حمله — اجراکردنش راه کلاسیک آلوده‌کردن سیستم خودت است. **اجرا نمی‌شود.**
- ✅ **جایگزین قانونی و امن برای کارهای واقعی:** `scrcpy` (آینه‌کردن و کنترل گوشی خودت روی کامپیوتر) + `adb` (بکاپ، انتقال فایل، اتوماسیون) — رایگان، متن‌باز، بدون Metasploit.

---

## ⛔→✅ دانلود از یوتیوب: بسته بود، **حل شد** (۱۴ اکتبر ۲۰۲۶)

- **علت بسته‌بودن:** بلاک IP دیتاسنتری توسط گوگل («Sign in to confirm you're not a bot»).
- **راه‌حل کارآمد:** تونل WireGuard رایگان در فضای کاربر به **Cloudflare WARP** (بدون اکانت، بدون root): `wgcf register` + `wireproxy` در `/opt/data/workspace/tools/warp` (اجرا: `bash start_warp.sh` → SOCKS5 روی `127.0.0.1:25344`). بعد: `yt-dlp --proxy socks5h://127.0.0.1:25344 ...`
- **نکتهٔ فنی:** wireproxy فلگ `-p` ندارد؛ پورت در بخش `[Socks5]` فایل کانفیگ تعریف می‌شود.
- **تأییدشده:** IP خروجی کلادفلر شد، یوتیوب ۲۰۰ داد، یک AMV 2:24 به‌صورت **1080p (۱۵MB)** + **mp3 192k (۳٫۴MB)** دانلود شد.
- **ربات دانلودر قدیمی** (`workspace/telegram-downloader`) هم باید با همین پروکسی اجرا شود، وگرنه دقیقاً همین‌جور بلاک است.
- ❌ **این‌ها دیگر امتحان نشوند:** ۸ کلاینت yt-dlp · ۷ نمونهٔ Invidious · ۶ API Piped · ۴ پروکسی CORS · cobalt · APIهای عمومی دانلود — همه ۴۰۳/۴۰۱/۵۰۰.

---

## ❌ ردشده / دروغ

- **«Higgsfield AI متن‌باز و رایگان»** (ریل اینستاگرام، اکتبر ۲۰۲۶): ادعای «رایگان + متن‌باز» **دروغ** بود؛ Higgsfield خودش پلتفرم اشتراکی پولی است. آن ریل طعمهٔ کامنت/فالوور بود.

---

## ✅ Wikimedia Pageviews REST API — spike-detection با عدد واقعی (بررسی‌شده ۱۴ اکتبر ۲۰۲۶)

- **چیستی:** API رسمی بنیاد ویکی‌مدیا که **بازدید روزانهٔ/ماهانهٔ هر مقالهٔ ویکی‌پدیا** را می‌دهد. بدون کلید، بدون ثبت‌نام، بدون سهمیه‌ای که ما دیده باشیم.
- **نمونهٔ فراخوانی:**
  `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/<Article>/daily/2026092800/2026101400`
  (بازگشت JSON: آرایهٔ `{timestamp, views}`) · ماهانه: `.../monthly/2026010100/2026101400`
- **تست واقعی امروز:** مقالهٔ `Superhabitable_world` → ۱۳ اکتبر ۲۰۲۶ = **۴۲۵** بازدید، ۱۲ اکتبر = ۱۶۶، و ۷۷–۱۴۷ برای ۱ تا ۱۱ اکتبر = جهش ۳ تا ۵ برابری روی روزِ خبرِ نیویورک‌تایمز. همین روش ثابت کرد `Kinetic_energy` صاف است (۶۶۹–۹۷۹ در روز) → یعنی ترندِ «collision» هیچ جهشی ندارد.
- **قیمت:** رایگان. **محدودیت واقعی:** فقط ترافیک ویکی‌پدیا را می‌بیند (نه گوگل/یوتیوب) و نویز دارد؛ برای «قله» خوب است، برای «حجم بازار» نه.
- **چرا مهم است برای ما:** ارزان‌ترین راه برای گفتن «این ترند واقعاً همین امروز جهش کرد، با عدد و نه حس».

---

## ✅ Google Trends daily RSS — ترند روز + عدد جست‌وجو (بررسی‌شده ۱۴ اکتبر ۲۰۲۶)

- **چیستی:** خوراک RSS رسمی ترندهای روز گوگل به تفکیک کشور: `https://trends.google.com/trending/rss?geo=US` (همچنین `DE`, `AT`). هر آیتم `<title>` + تگ `ht:approx_traffic` (مثل «500+»).
- **تست واقعی امروز (۱۲:۳۱ UTC):** لیست US شامل `superhabitable world [500+]` (آیتم اول)، `collision [200+]`، `steven bartlett [500+]`، `ms stock [500+]`، `tommy paul [500+]` بود. لیست AT شامل `aryna sabalenka` و `stefanos tsitsipas` (تنیسِ روز).
- **قیمت:** رایگان، بدون کلید. **محدودیت واقعی:** فقط ~۱۰ آیتم در هر کشور، مرتب‌شده و بی‌نمودارِ زمانی؛ عدد فقط «۵۰۰+» است نه مقدار دقیق، و در طول روز عوض می‌شود. برای «حجم نسبتاً» باید با یک منبع دوم (بالا) تأیید شود.
- **نکتهٔ مهم برای ما:** این خوراک همان منبعی است که `trend-radar/trend_scout.py` استفاده می‌کند؛ ولی خودِ خوراک علت ترند را نمی‌گوید (مثلاً `collision` = خبر تصادف جاده‌ای بود، نه فیزیک) → علت را همیشه جدا سرچ کن.

---

## چطور مدخل جدید اضافه شود

۱. ادعای فوروارد را با جست‌وجو و (در صورت امکان) با باز کردن خودِ سرویس در مرورگر بررسی کن — نه با نقل‌قول.
۲. اگر سرویس قابل تست زنده بود، در مرورگر واقعاً یک پیام بفرست تا رایگان‌بودن را ببینی.
۳. قیمت، محدودیت واقعی (سقف/اکانت/سیستم‌عامل)، و تاریخ بررسی را بنویس.
۴. اگر ادعا دروغ بود، زیر «ردشده» ثبت کن تا دوباره وقت تلف نشود.

## ⚪ StarkLLM — github.com/homomorphicprivacy/StarkLLM (فوروارد @RepoFA، ۱۴ اکتبر ۲۰۲۶)

- **چیستی:** دستیار هوش مصنوعی **محلی** با RAG روی اسناد خودت (چت با فایل‌ها، Workspace، Knowledge Base، MCP host، جست‌وجوی سراسری، TTS داخلی) روی **Ollama** — با ادعای «معماری صفر-ابری».
- **واقعی است؟** ✅ بله، پروژهٔ واقعی و نسبتاً جدی است: ۱۴۴ فایل، بک‌اند FastAPI + مهاجرت‌های alembic، فرانت React/Vite، Docker Compose، نصب‌کنندهٔ Inno Setup برای ویندوز. Apache-2.0 (در README؛ فایل LICENSE در ریپو دیده نشد). کامیت آخر ۱۲ اکتبر ۲۰۲۶.
- **وضعیت واقعی (هشدار):** **۰ ستاره · ۰ فورک · ۱ مشارکت‌کننده** · ساخته‌شده ۲۷ اوت ۲۰۲۶ → پروژهٔ کاملاً تازه و بدون جامعه/آدیت.
- **محدودیت‌های سخت:** فقط **ویندوز ۱۰/۱۱ + WSL2 + Docker Desktop** (نصب‌کننده‌اش `.exe/.iss`). مدل پیش‌فرض `qwen3.8:27b` (نیازمند GPU جدی)؛ حداقل ۸GB RAM برای مدل ۳B. یعنی روی سرور headless ما **بدون GPU** عملاً قابل استفاده نیست.
- **برای ما چه ارزشی دارد؟ تقریباً هیچ.** همان قابلیت را **Hermes خودمان** دارد (حافظه + مهارت‌ها + جست‌وجوی سشن + ابزار وب) و هیچ مسیر درآمدی هم ندارد (رایگان/متن‌باز است).
- ⭐ **تنها چیز ارزشمند این ریپو:** مدل صدای **Piper** (`de_DE-thorsten-medium.onnx`) که داخلش بسته شده بود → به‌عنوان **جایگزین آفلاین edge-tts** برداشتیم. تست شد: صدا در انگلیسی و آلمانی **بدون شبکه و بدون کلید** ساخته می‌شود (`/opt/data/workspace/tts-offline/voices/`، pip: `piper-tts`). الان fallback خودکار خط تولید ویدیو است؛ اگر edge-tts مثل امروز 403 بدهد، تولید ویدیو نمی‌خوابد.

---

## ⚪ AIDahl — github.com/mohsen-niksirat/AIDahl (فوروارد @RepoFA، ۱۵ اکتبر ۲۰۲۶)

- **چیستی:** ربات تلگرام پایتونی «دستیار AI شخصی» با **BYOK** (کاربر کلید API خودش را میدهد) برای OpenRouter/Groq/Mistral/Cerebras/SiliconFlow/GitHub Models + سرویس «Dahl» + حالت «Manus Agent» (تصویر/ادیت/پژوهش). ذخیره‌سازی روی **Supabase** و استقرار رایگان روی **Deployka**؛ راهنمای فارسی نصب (`docs/SETUP_FA.md`) + سیاست حریم خصوصی.
- **وضعیت:** ✅ واقعی است (کلاهبرداری نیست). ساخت ۲۰ سپتامبر ۲۰۲۶، آخرین کامیت همان روز (از آن وقت راکد)، **۴ ستاره · ۰ فورک**، **بدون فایل لایسنس**.
- **بررسی کد (۱۴۰۵):** یک فایل `main.py` با **۵٬۰۹۹ خط / ۱۹۸KB** (یکپارچه)، فقط ۳ وابستگی (`pyTelegramBotAPI`, `httpx`, `python-dotenv`).
  - ✅ **هیچ کلید/توکن هاردکدشده‌ای پیدا نشد**؛ ادمین‌ها از env می‌آیند.
  - ✅ دامنه‌های خروجی همان سرویس‌های انتظاری‌اند (openrouter.ai, api.groq.com, api.mistral.ai, api.cerebras.ai, api.siliconflow.cn, models.github.ai, api.telegram.org, manus.im/api.manus.ai, inference.dahl.global). هیچ ارسال داده به دامنهٔ ناشناس دیده نشد.
  - ⚠️ **ریسک اصلی — کلیدها رمزنگاری نمی‌شوند:** جدول `public.user_api_keys` ستون `api_key text` دارد و در کل کد هیچ `encrypt/fernet/pgcrypto/hashlib` وجود ندارد → **کلید هر کاربر به‌صورت متن خام در دیتابیس است** و هر کسی که ربات را deploy کند (اپراتور) می‌تواند همه را بخواند. RLS روشن است ولی policy عمومی ندارد، یعنی فقط بک‌اند (= همان اپراتور) دسترسی دارد.
- **برای ما ارزش عملی ندارد:** همان کار را Hermes با مدیریت کلید خودمان بهتر انجام می‌دهد (و ما بروکرِ کلیدِ دیگران نمی‌خواهیم). مسیر درآمدی هم ندارد مگر «راه‌اندازی برای دیگران» که احمد رد کرده.
- ⭐ **تنها چیز قابل برداشت:** الگوی «Deployka + Supabase = استقرار رایگان ربات کوچک» و فهرست ارائه‌دهنده‌های ارزان/رایگان inference (Cerebras، SiliconFlow، GitHub Models) — اگر خواستیم زنجیرهٔ fallback مدل‌های خط تولید ویدیو را قوی‌تر کنیم، اینها گزینه‌های اضافه‌اند.

---

## ✅/⚠️ Lunel — github.com/ArasTey/lunel (فوروارد @RepoFA، ۱۵ اکتبر ۲۰۲۶)

- **چیستی (دقیق):** این یک ابزار AI نیست — یک **پلتفرم پروکسی چندکاربره** است: «Lunel Core» = رانتایم پروکسی که **VLESS (WebSocket + xHTTP)، Trojan (WS + xHTTP) و Shadowsocks AEAD روی WebSocket** را با **سهمیهٔ ترافیک و انقضا به‌ازای هر لینک** سرو می‌کند؛ «Console» = پنل وب مدیریت (ورود GitHub OAuth، ویزارد ۶ مرحله‌ای، متریک/لاگ زنده، پنل ادمین، PostgreSQL)؛ «Worker» = ایجنت گره که نمونه‌ها را در **کانتینر ایزولهٔ Docker** اجرا می‌کند. مشتق‌شده از «RVG Gateway».
- **وضعیت:** ✅ واقعی و جدی — **۱٬۰۵۶ ستاره · ۲٬۵۲۴ فورک** (فورک‌های زیاد از الگوی «fork کن → روی Railway دیپلوی کن» می‌آید، نه فورک‌فارم) · ۹۵ فایل · آخرین کامیت ۲ اکتبر ۲۰۲۶ · لایسنس MIT + notice نرم‌افزار مشتق. کامیت «iran reachability ping» نشان می‌دهد بازار هدفش ایران است.
- **استقرار:** فورک → یک سرویس روی Railway/Render با `python main.py` (SQLite داخلی، بدون متغیر لازم) — یعنی نیازی به سرور ما ندارد.
- **⚠️ ریسک‌ها:** (۱) **یوزر/پس پیش‌فرض `admin`/`admin`** روی پنل — اگر عوض نشود، هر کسی دامنه را پیدا کند کنترل همهٔ نمونه‌ها را می‌گیرد. (۲) سرویس عمومی پروکسی = عبور ترافیک دیگران از دامنهٔ تو → ریسک ToS هاست، سوءاستفاده، و حساسیت قانونی. (۳) ماهیتاً یک **کسب‌وکار فروش VPN** است، نه ابزار شخصی.
- **برای ما:** فعلاً هیچ — احمد گفت فقط روی کانال تمرکز کنیم. اما اگر روزی «خط درآمد دوم» خواست، این کیتِ آمادهٔ پنل فروش VPN است (با همان هشدارها).

---

## ⚠️ qwen-free-api — github.com/Godde3s/qwen-free-api (فوروارد @RepoFA، ۱۵ اکتبر ۲۰۲۶)

- **چیستی:** بریج (پل) غیررسمی که حساب وب `chat.qwen.ai` را به اندپوینت‌های سازگار با **OpenAI و Anthropic** تبدیل می‌کند — یک باینری Go، استخر چند-اکانتی، tool calling، داشبورد فارسی. «Ported from GLM-Free-API».
- **وضعیت:** ✅ واقعی — Go، **MIT**، ۲۹ ستاره · ۴ فورک · ۱ مشارکت‌کننده. ساخت ۸ سپتامبر ۲۰۲۶ و **عملاً از ۹ سپتامبر متوقف** (آخرین کامیت واقعی v1.0.2).
- **چطور کار می‌کند (مهم):** داخل ریپو ابزارهای **شکستن محافظت‌های ضد-ربات علی‌بابا** هست: `AliyunCaptcha.js` (۲۲۴KB)، `feilin087….js` (۵۵۸KB)، `VM_hash_gen_report.md`، یک پوشهٔ کامل دیکامپایل VM (`vm_hash_decompile_scripts/`)، `captcha_param_gen.py`، `signature_gen.py`، `qwen-bx` (هدرهای واقعی **Baxia**) + `zai_client.py`. یعنی دسترسی «رایگان» از راه **دور زدن کپچا/امضای ضد-ربات** به‌دست می‌آید، نه از یک API رسمی.
- **⚠️ ریسک‌ها:** (۱) **نقض آشکار ToS چت‌کیوئن** — اکانت‌های وب که در استخر می‌گذاری در معرض بن هستند. (۲) برای کار کردن باید **کوکی/توکن حساب وب خودت** را بدهی؛ هر کس این سرویس را اجرا کند آن اعتبارنامه‌ها را در دست دارد. (۳) قطعات مبهم ۵۰۰KB+ و بایت‌کد در ریپو → قابل آدیت نیست. (۴) شکننده: به مکانیزم‌های مهندسی‌معکوسِ متغیر وابسته است و بی‌صدا می‌شکند؛ پروژه هم سه هفته است مرده. (۵) در برخی کشورها دور زدن «اقدامات فنی حفاظتی» می‌تواند مسئلهٔ حقوقی داشته باشد.
- **برای ما: ❌ استفاده نکنیم.** وسوسه‌اش هست (Qwen3.8-Max مجانی برای fallback خط تولید)، ولی ما به fallback **پایدار و قانونی** نیاز داریم، نه اکانت‌های در معرض بن. گزینهٔ درست: افزودن ارائه‌دهنده‌های رسمیِ رایگان/ارزان (Cerebras، SiliconFlow، GitHub Models، Groq، Mistral) به زنجیرهٔ مدل.

---

## ✅ ai-website-cloner-template — github.com/JCodesMore/ai-website-cloner-template (فوروارد @RepoFA، ۱۶ اکتبر ۲۰۲۶)

- **چیستی:** تمپلیت Next.js 16 + React 19 + Tailwind v4 + shadcn برای «کلون کردن هر سایتی با یک پرامپت» با ایجنت کدنویس.
- **وضعیت:** ✅ واقعی و جدی — MIT، **۳۶٬۸۵۴ ستاره**، ۵٬۴۲۱ فورک، ۲ فعال، آخرین پوش ۵ اکتبر ۲۰۲۶. (تخمین تصویر «۱۵ مشارکت‌کننده» نزدیک بود.)
- **نکتهٔ مهم:** **این را از قبل داشتیم.** مهارت `clone-website` نصب‌شدهٔ ما با نسخهٔ فعلی ریپو **بایت‌به‌بایت یکسان** است (SKILL.md و هر دو reference: `inspection-guide.md`، `framer-and-motion.md` — با هش مقایسه شد، یکسان). پس «یادگیری» چیزی نداشت.
- **کاری که کردم:** خودِ تمپلیت را به‌صورت پروژهٔ آمادهٔ اجرا کلون کردم → `/opt/data/workspace/website-cloner` (۲.۵MB). حالا کلون هر سایت یک دستور است.
- **تله‌ای که ریپو خودش هشدار می‌دهد:** Next.js نصب‌شده نسخهٔ جدید با تغییرات شکننده است — قبل از کدنویسی `node_modules/next/dist/docs/` را بخوان، نه حافظهٔ مدل را.

---

## 🧠 Hindsight — github.com/vectorize-io/hindsight (فوروارد احمد، ۱۶ اکتبر ۲۰۲۶)

- **چیستی:** سیستم حافظهٔ ایجنت‌ها: چهار شبکهٔ منطقی (world/experience/observation/opinion) و سه عمل `retain` / `recall` / `reflect`. حافظه‌ها در «بانک» ذخیره می‌شوند؛ چند ایجنت می‌توانند به **یک بانک مشترک** وصل شوند. سرور MCP روی `http://localhost:8888/mcp/<bank_id>/`.
- **وضعیت:** ✅ واقعی و پشتوانه‌دار — MIT، **۵۰٬۲۵۰ ستاره**، ۶٬۰۹۵ فورک، v1.0.0 (۱۳ اکتبر ۲۰۲۶)، مقالهٔ ACL 2026 (LongMemEval ۹۱.۴٪ با Gemini-3 Pro)، بازتولید مستقل توسط Virginia Tech و Washington Post.
- **نصب:** (۱) داکر `ghcr.io/vectorize-io/hindsight:latest` + پستگرس داخلی، (۲) **بدون داکر:** `pip install hindsight-all` (سرور امبد). نیاز به **کلید LLM**: openai/anthropic/gemini/groq/ollama/lmstudio/minimax.
- **وضعیت محیط ما (سنجیده‌شده):** داکر نصب است ولی **دیمنش خاموش** است؛ RAM ۷.۸GB (۴.۶ آزاد)، دیسک ۱۹۳GB آزاد، ۶ هسته؛ Hermes از MCP پشتیبانی می‌کند؛ کلید رایگان Groq موجود است.
- **حکم:** ارزش امتحان دارد — برای ۵ بات ما یک بانک حافظهٔ مشترک می‌سازد که امروز با فایل‌های outbox دستی ردوبدل می‌شود. **مسیر پیشنهادی:** نصب امبد با pip + کلید Groq (بدون داکر، بدون هزینه)، تست retain/recall، بعد وصل کردن به‌عنوان MCP.

---

## watermarks-remover (guillaumemeyer) — verified 2026-10-17
- **Source:** https://github.com/guillaumemeyer/watermarks-remover — MIT, 24.3k stars / 2.8k forks,
  created 2026-08-11, release v0.7.0, clone 3.9 MB, deterministic layer is stdlib-only Python.
- **What it actually does:** strips *AI provenance* marks, not visible logos.
  (A) text: invisible Unicode, bidi overrides, tag chars, space homoglyphs — deterministic;
  (B) files: C2PA / EXIF / XMP / doc properties for PNG, JPEG, PDF, DOCX, XLSX, PPTX, EPUB,
  MP4/MOV, MP3/WAV/FLAC — deterministic;
  (C) statistical (token-sampling) text watermarks — needs an LLM rewrite pass.
- **Tested on this box** (`service/scripts/inspect_text.py`, `clean_file.py`):
  English sample with 5 hidden marks -> all 5 removed + NBSP replaced (51 -> 46 chars).
  **Persian sample with 4 ZWNJ survived intact (4/4) and the injected ZWSP was removed** — the
  cleaner treats script joiners as "load-bearing invisibles" and keeps them, so it will not break
  our Persian half-spaces.
- **Caveats:** (1) our pipeline is procedural + edge-tts + stock photos, so we currently carry no
  AI provenance marks — value today is metadata hygiene (EXIF/XMP/C2PA, tag chars) on our exports;
  (2) it is a provenance-removal tool: YouTube requires disclosure of altered/synthetic content and
  the EU AI Act transparency duties apply in Germany — use it on our own files for privacy, never
  on third-party content; (3) it ships as a Claude Code skill + local HTTP service (port 8765);
  to use it as a Hermes skill, adapt it with the `external-skill-import` skill.
- **Verdict:** real and safe to run locally. Deterministic layer worth wiring in for metadata
  cleanup; skip the Docker/LLM layers unless a specific need appears.

## Toonkit (toonkit.io) + the three video models from that ad — verified 2026-10-17
- **Domain:** registered 2025-10-20 (expires 2029), live, EN/KO pages, IP 49.50.129.158 (KR).
  Positioning: "AI Anime Production Studio — Storyboard to Video"; Canvas / Storyboard / Playground,
  Claude-MCP + ChatGPT-plugin pages, update notes dated 2026.10.16 (mentions Sora 2 / Sora 2-Pro,
  GROK, QWEN, SUNO).
- **Pricing (read live):** Free $0 — **"300 credits at signup", ~60 images or ~6 videos**, and the
  tier lists commercial use / custom style / watermark removal (verify in-app before publishing);
  Starter $13.90->$9.90/mo (900 credits, ~18 videos 1080p); Standard $44.90->$29.90 (3,000 credits,
  ~60 videos); Standard Plus $74.90->$47.90 (5,200 credits). The ad's "300 free credits" is TRUE.
- **The three models are real:**
  Seedance 2.5 = ByteDance Seed official (30 s audio+video joint generation, seed.bytedance.com/en/seedance2_5);
  Wan 3.0 = Alibaba Tongyi Lab, public beta since 2026-08-06, API $0.05/s (480p) / $0.10/s (720p);
  MiniMax H3 (= Hailuo 3.0) = **OPEN-WEIGHTS** multimodal video model, 2K/24fps, 5-15 s clips with
  native stereo audio, live since 2026-07-31 (minimax.io/blog/minimax-h3).
- **Cost reality for a clone:** 30 s of 720p on Wan 3.0 = ~$3 of raw API cost, so ~6 free videos per
  signup = ~$9-18 eaten as acquisition spend. A paid-API wrapper is a funded-business play; we cannot
  subsidise it. The buildable-and-free path is running open-weight models (MiniMax H3 / Wan) on our
  OWN GPU — that is what the planned rig buys us.
- **Verdict:** real platform, real models, real free credits; links from such channels are affiliate.
  Action worth taking: spend the 300 free credits on 3-5 test prompts to benchmark against our own
  procedural pipeline before any money moves.

---

## ✅ SlipNet — `github.com/anonvector/SlipNet` (ضدسانسور، ایران) — بررسی ۱۷ اکتبر ۲۰۲۶

- **اصلاح نام:** اپی که در اسکرین‌شات گوشی احمد بود **SlipNet** است، نه SplitNet. (آیکون تیره با خطوط قرمز/سفید مورب، ردیف سوم.)
- **چیستی:** کلاینت VPN اندروید برای شبکه‌های سانسورشده — تونل ترافیک داخل **DNS** و چند پروتکل دیگر. Jetpack Compose + Kotlin؛ نسخهٔ CLI هم برای مک/لینوکس/ویندوز به Go. ~۱ هزار ستاره، آخرین ریلیز **v2.5.5** (۲۶ مه).
- **پروتکل‌ها:** DNSTT / NoizDNS / VayDNS (تونل DNS + مقاوم به DPI) · Slipstream (QUIC) · SSH · NaiveProxy · VLESS (CDN/Cloudflare) · DoH · Tor. حالت‌های `+ SSH` برای نشتی‌صفر.
- **تمرکز ایران:** اسکنر داخلی resolver با لیست‌های DNS ایران («IR DNS Lite» و «IR DNS Ranges») + Geo-bypass. یعنی مکمل v2rayNG/v2RayTun؛ ابزار همین تیم.
- ⚠️ **بدون سرور کار نمی‌کند:** باید خودت **SlipGate** (نصب‌کنندهٔ یک‌خطی روی VPS ~۵ دلاری، همهٔ پروتکل‌ها + VLESS) راه بیندازی و لینک `slipnet://` را در اپ پیست کنی — یا پروفایل از یک اپراتور بگیری.
- ⚠️ **دانلود فقط از GitHub Releases یا کانال رسمی تلگرام `@SlipNet_app`.** در Google Play/App Store نیست → هر APK از منبع دیگر ریسک بدافزار دارد.
- **وضعیت فعالیت (API گیتهاب، ۱۷ اکتبر ۲۰۲۶):** ۱٬۴۹۲ ستاره · ۱۳۹ فورک · ۳۹ ایشوی باز · آرشیو نشده. آخرین **ریلیز: v2.5.5 — ۲۶ مه ۲۰۲۶** (تنها ۲ ریلیز در گیتهاب دارد؛ نسخه‌های قدیمی‌تر از تلگرام پخش شده‌اند). آخرین **کامیت: ۲۱ اوت ۲۰۲۶** → حدود ۲ ماه بدون تغییر کد، ~۵ ماه بدون ریلیز.
- ⚠️ **لایسنس به‌روزرسانی شد:** از ۲۱ اوت ۲۰۲۶ خودِ نویسنده لایسنس را به **GNU AGPL-3.0** تغییر داد (commit: «Replace SlipNet license with GNU AGPL v3»). یعنی الان واقعاً **open-source** است — ادعای قبلی «source-available» منقضی شده. (راهنمای USER_GUIDE در مخزن هنوز متن قدیمی «source-available» را دارد — ناسازگاری داخلی دارد.)
- **ربطی ندارد به:** «SplitNet 2.0» (اپ iOS اسپلیت‌اسکرین، سازنده: csaba abel) و «SplinterNet» (پیام‌رسان بلوتوثی پروژهٔ Watkinson/Hall).
- **کاربرد برای ما:** ابزار ایرانی‌هاست؛ احمد ساکن آلمان است و برای خودش لازم ندارد — فقط اگر بخواهیم برای خانواده/آشناها در ایران دسترسی بسازیم (VPS آلمان + SlipGate).

---

## 🎬 motionmaxxing — GitHub: `Tejashmakwana/motionmaxxing` (تست واقعی روی سرور، ۱۹ اکتبر ۲۰۲۶)

- **چیستی:** «مهارت ایجنت» (SKILL.md + references + رانتایم GSAP) برای ساخت موشن‌گرافیک حرفه‌ای با **HTML/CSS/JS**، رندر با **کروم هدلس + ffmpeg**. Apache-2.0، ~۸۷۵ ستاره، ۸۱ فورک.
- ⚠️ **پروژه مرده نیست ولی نگهداری نمی‌شود:** ساختهٔ ۶ اکتبر ۲۰۲۶، فقط **۲ کامیت** (هر دو همان روز)، از آن زمان هیچ. «Early release» خودش اعتراف کرده. داخل محصول تجارتی FinalMotion زندگی می‌کند.
- ✅ **تست واقعی ما:** کلون شد در `/opt/data/workspace/motionmaxxing`، یک استینگ عمودی ۶ ثانیه‌ای DOPEAK (۱۰۸۰×۱۹۲۰) از صفر نوشته و رندر شد → **۲۰ ثانیه رندر برای ۶ ثانیه ویدیو** (~۱۰ فریم/ثانیه رندر). خروجی: `out/dopeak-final.mp4` (790KB).
- 🔧 **نکتهٔ سرور (مهم برای هر بار نصب):** کروم روت بدون `--no-sandbox` کرش می‌کند. راه‌حل: رَپر `out/chrome-nosandbox.sh` و `CHROME_PATH` به آن اشاره کند. کروم موجود: `/opt/hermes/tools/chromium-1208/chrome-linux64/chrome`.
- ✅ **گیت‌های خودش واقعاً کار می‌کنند:** `look.py` قفل‌شدن ۱٫۵۷ ثانیه‌ای پایان و آمار ۳۲٪ فریم آخر را گرفت (FAIL → پس از اصلاح PASS)؛ `lint.mjs` نوارِ رشدکنندهٔ من را به‌درستی «progress bar» تشخیص داد. این تنها ابزاری است که تا حالا خروجی خودش را نقد کرده.
- ⚠️ **محدودیت‌ها:** GPU ندارد → WebGL سنگین کُند؛ ElevenLabs لازم برای صدا (بدون کلید = فیلم بی‌صدا)؛ D1 (چیدمان تیتر چپ‌چین) هنوز روی کامپ من FAIL می‌دهد — قاعده‌اش سختگیرانه است. میانگین حرکت ۲٫۸ در برابر باند انسانی ۶٫۸ → کامپ من زیاد ساکن است، نه ابزار.
- **کاربرد برای ما:** ارتقای بصری شورت‌های DOPEAK از اسلاید+zoompan به موشن‌تایپ واقعی. ارزش دارد در پایپ‌لاین بیاید، ولی به‌عنوان **مهارت خودمان** (فایل‌ها را داریم، پروژه آپدیت نمی‌شود).


---

## 🧪 Harness² — `github.com/google-research/harness2` (بررسی ۱۹ اکتبر ۲۰۲۶)

- **چیستی:** فریم‌ورک پژوهشی گوگل برای «هارنس‌کردن بازگشتی» ایجنت‌ها: بدون تغییر وزن مدل، ۸ جزء هارنس (system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins) به‌صورت خودکار ویرایش و A/B می‌شود. حلقه: Propose → Probe → Compose + «improvement harness» پایدار که درس‌های هر تسک را نگه می‌دارد.
- **واقعی است:** arXiv 2610.14224 · سایت harness2.github.io · Apache 2.0. ولی خودشان نوشته‌اند «not an officially supported Google product» → کد پژوهشی، نه محصول.
- **نتایج ادعایی:** تا +11.5 در WorkBuddy-Bench، +4.5 در JobBench، +11.8pp در LAB با یک مرحله (GLM-5 و Gemini 3.5 Flash).
- ⚠️ **موانع استفادهٔ مستقیم برای ما:** Python 3.12 + uv، Node 20+، **Vertex AI / gcloud** برای اجرای مدل‌محور، Docker برای WorkBuddy؛ executor فقط OpenCode و Codex؛ بنچمارک‌هایش هم JobBench/LAB/WorkBuddy است. با Hermes + ollama-cloud قابل وصل‌شدن نیست و هر تسک k بار اجرا می‌شود → توکن‌بر.
- ✅ **چیز ارزشمند برای ما ایده است، نه نصب:** حلقهٔ «چند نسخهٔ ویرایش مهارت/پرامپت را روی همان تسک امتحان کن و برنده را نگه دار» — همان کاری که الان دستی با skill_manage/memory می‌کنیم. ارزش دارد به‌صورت سبک در فلوی مهارت‌ها کپی شود (نسخه A/B برای تسک‌های سخت).
- **درآمد:** صفر مستقیم. فقط قابلیت اطمینان ایجنت را چند پوینت بالا می‌برد.
- 🧪 **تست واقعی (۱۹ اکتبر ۲۰۲۶):** کلون شد در `/opt/data/workspace/harness2`، venv با Python 3.12 ساخته و `uv pip install -e '.[render]'` نصب شد (۸ پکیج). `harness2-demo --output runs/demo --k 2` بدون هیچ کلیدی اجرا شد: **۲ تسک، ۰ خطا، ۲۸ execution، ۳۲ editor call** — هم parallel و هم sequential.
- **خروجی دمو چه چیزی ساخت:** `base/` (هارنس پایه)، `library/k2/{agg,seq}/<domain>/INDEX.md` (ایندکس با cue)، و برای هر تسک `EXPERIENCE.md` با adopted harness + «what each edit did» + «Transferable lesson» با evidence و confidence. یعنی الگوی «درسِ مستندشده» را واقعاً تولید می‌کند.
- ⚠️ **ولی:** ادیتورهای دمو deterministic و اسکریپت‌شده‌اند، نه مدل. مسیر مدل‌محور (JobBench/LAB/WorkBuddy) به Vertex AI + gcloud + Node 20 + Docker/Pandoc/Poppler و مدل پولی نیاز دارد → با ollama-cloud وصل نشد و برای ما فعلاً بی‌صرفه است. **نصب ماند، ولی در فلوی کاری وصل نشد.**


---

## 🌐 Wispbyte — `wispbyte.com` (بررسی ۲۰ اکتبر ۲۰۲۶، از ریلز barnamenevisiinsta)

- **ریلز چه می‌گوید:** «هاست رایگان می‌خواید؟ این پست مال شماست» — ویدیو در واقع اسکرین‌رکورد صفحهٔ Wispbyte است (شعار: «A byte of possibility»، «Host the thing that's been stuck on localhost»). صفحهٔ فارسی‌زبان برنامه‌نویسی، تبلیغ/ریفِرال است، نه معرفی بی‌طرف.
- **واقعی است:** شرکت از ۲۰۲۳ (قبلاً PylexNodes)، دفتر/سرور رومانی (Bacău). Trustpilot: **۴٫۵/۵ از ۶۳۷ نظر**، پروفایل claim شده. Gridinsoft 95/100، Scamadviser بدون فلگ جدی.
- **پلن رایگان:** ۵۱۲MB RAM + ۱GB دیسک، بدون کارت بانکی، بدون تبلیغ اجباری، ۲۴/۷. شرط: **هر ۱۴ روز یک‌بار لاگین** وگرنه پاک می‌شود. فقط سرور رومانی. پشتیبانی فقط فروم/دیسکورد.
- **پرمیوم:** از €۴٫۹۹/سال (توصیه‌شده €۹٫۹۹) — یعنی «رایگان» قیف فروش است.
- ⚠️ **شکایت‌های تکرارشده در نظرات:** دان‌تایم ناگهانی، لگ پنل، پشتیبانی کند. بدون SLA در پلن رایگان.
- **کاربرد برای ما:** فقط آزمایش/پروژهٔ دورریختنی (وب‌هوک تست، بات کوچک). زیرساخت درآمدی یا چیزی با دادهٔ حساس را هرگز روی پلن رایگانش نمی‌بریم.

- ✅ **تست واقعی پلن رایگان (۲۰ اکتبر ۲۰۲۶):** سرور `smoke-test` روی نود **FREE-EU-RO-09**، پایتون **3.11.17**، پورت عمومی از متغیر `SERVER_PORT` تزریق می‌شود. آدرس عمومی `78.154.103.14:16329` → `/` و `/health` هر دو **HTTP 200** با ~۹۰ms از آلمان. آپلود از تب Files، اجرا با `python main.py` در Startup. یعنی ادعای «رایگان ۲۴/۷ با پورت عمومی» واقعی است.


---

## 🐟 MiroFish — `github.com/666ghj/MiroFish` (بررسی ۲۰ اکتبر ۲۰۲۶، ریلز @aradazr.dev)

- **ریلز چه می‌گفت (پیاده‌شده از صدا):** ابزار اوپن‌سورسی که «هزار مشتری فیک» را قبل از لانچ به سمت محصولت می‌فرستد؛ لندینگ، قیمت یا تبلیغت را می‌دهی و می‌پرسد مردم عاشقش می‌شوند یا رد می‌شوند؛ هزار ایجنت با پرسونا و حافظهٔ مستقل (دانشجو، سرمایه‌گذار، بازنشسته...) هر کدام جدا تصمیم می‌گیرند. CTA: کامنت «جمعیت» تا لینک در دایرکت بیاید.
- **واقعی است:** ۸۰٬۷۶۹ ستاره، ۱۲٬۲۵۳ فورک، Python، **AGPL-3.0**، ساخت ۲۰۲۵-۱۱، آخرین پوش ۱۶ اکتبر ۲۰۲۶. پشتش Shanda Group. سایت mirofish.ai. (ریلز «۷۳ هزار» گفته بود — عدد قدیمی‌تر است، الان بیشتر.)
- **چطور کار می‌کند:** مواد اولیه (گزارش/خبر/لندینگ) → استخراج موجودیت‌ها و ساخت گراف دانش (Neo4j) → ساخت دنیای موازی با صدها-هزاران ایجنت LLM که با هم تعامل می‌کنند → گزارش پیش‌بینی. نسخهٔ آفلاین: `nikmcfly/MiroFish-Offline` (Neo4j + Ollama).
- ⚠️ **هزینه و محدودیت:** هر اجرا صدها-هزاران فراخوانی LLM است؛ بدون GPU/مدل محلی گران و کند می‌شود. روی سرور ما (۷٫۸ گیگ رم، بدون GPU) نصب سنگین است و با ollama-cloud هم هزینه‌بر.
- ⚠️ **ادعا را کوچک کنید:** «مشتری فیک» = شبیه‌سازی پرسونا با LLM، نه تقاضای واقعی. برای مقایسهٔ A/B پیام و قیمت مفید است؛ برای «آیا محصول می‌فروشد» جای تست واقعی را نمی‌گیرد.
- **کاربرد بالقوه برای ما:** قبل از لانچ یک لندینگ/قیمت/تامبنیل، ۳-۴ نسخه را با پرسوناهای هدف بسنجیم. فقط بعد از اینکه چیز قابل‌فروشی داشتیم.


---

## 🕷 ScrapeGraphAI — `github.com/ScrapeGraphAI/Scrapegraph-ai` (بررسی ۲۰ اکتبر ۲۰۲۶، ریلز)

- **ریلز چه می‌گفت (از صدا):** ابزار رایگان AI برای استخراج داده از سایت‌ها؛ لینک سایت + یک توضیح سادهٔ فارسی می‌دهی و بعد ~۱ دقیقه لیست مرتب تحویل می‌گیری؛ ادعا: ۳۰ هزار ستاره، کاملاً رایگان، با Claude Code و Codex هم کار می‌کند.
- **واقعی است:** **۳۲٬۰۲۵ ستاره**، ۳٬۴۳۲ فورک، **MIT**، Python، آخرین پوش ۶ اکتبر ۲۰۲۶.
- ✅ **تست واقعی ما:** نصب شد در `workspace/scrapegraph-test` (Python 3.12 + `scrapegraphai` + `langchain-groq`)، روی `books.toscrape.com` با مدل `groq/openai/gpt-oss-120b` → **۲۰ کتاب با عنوان و قیمت** در یک اجرا. کار می‌کند.
- ⚠️ **«کاملاً رایگان» درست نیست:** خود کتابخانه MIT است، ولی هر اجرا توکن LLM مصرف می‌کند؛ رایگان‌بودن یعنی Groq free-tier یا Ollama محلی.
- 🔧 **دو تلهٔ نصب:** (۱) `langchain-groq` جدا نصب شود وگرنه ImportError. (۲) `PLAYWRIGHT_BROWSERS_PATH` سرور به `/opt/hermes/tools` اشاره می‌کند که نوشتنی نیست و `playwright install` تایم‌اوت می‌خورد → لینک کردن کرومیوم موجود به مسیر قابل‌نوشتن. جزئیات در مهارت `scrapegraph-ai`.
- **کاربرد برای ما:** استخراج سریع قیمت/فهرست/مشاغل از سایت‌هایی که پارسر نداریم؛ برای کرال انبوه نه (هزینهٔ توکن).


---

## 🔬 REA — `github.com/morluto/rea` (بررسی ۲۰ اکتبر ۲۰۲۶، ریلز + تست واقعی)

- **ریلز چه می‌گفت (از صدا):** ابزاری که «هر اپلیکیشن پولی یا رایگان را مهندسی معکوس می‌کند و برایت می‌سازد»؛ ادعا: مردم دارند ورد/پاورپوینت/فتوشاپ و حتی بازی‌ها را کلون می‌کنند، حالا به سورس‌کد دسترسی داریم، نسخهٔ شخصی‌سازی‌شده بساز. نصب ساده روی لپ‌تاپ، از طریق Claude Code یا Codex. CTA: لینک در کپشن.
- **واقعی است:** `morluto/rea` — **۳۴۵٬۷۷۳ ستاره**، ۸۷٬۱۱۵ فورک، **MIT**، TypeScript، آخرین پوش همان روز. توضیح رسمی: «Reverse engineer anything with agents, from app behavior down to native binaries.»
- ✅ **روی همین سرور از قبل نصب است:** ۲۰۹ ابزار MCP با پیشوند `rea` + مهارت `reverse-engineer-anything` (نسخه ۴۲).
- ⚠️ **ادعای ریلز اغراق است:** REA «کلون فتوشاپ نمی‌سازد». کاری که می‌کند: تحلیل ایستای باینری/JS/Electron/APK/فریمور، استخراج API و جریان داده، دی‌کامپایل، مقایسهٔ نسخه‌ها، مشاهدهٔ رفتار در زمان اجرا. ساخت محصول از روی آن کار خود ایجنت است، نه یک دکمه.
- ⚖️ **حقوقی:** مهندسی معکوس نرم‌افزار اختصاصی در بیشتر حوزه‌ها خلاف EULA و کپی‌رایت است؛ کلون‌کردن و توزیع، قطعاً. برای نرم‌افزار خودمان، اوپن‌سورس، یا تعامل‌پذیری مجاز، استفاده‌اش مسئله‌ای ندارد.
- 🧪 **تست ما:** روی `workspace/isometric-demo/dist` (اپ JS خودمان) اجرا شد؛ خط لوله کار کرد و Evidence با SHA-256 تولید کرد، ولی باندل مینیفای‌شدهٔ ۳۷۷KB سقف heap ورکر (۱ گیگ) را پر کرد و در تلاش دوم با `SIGKILL` کشته شد. یعنی روی این سرور (۲٫۵ گیگ رم آزاد) تحلیل باندل‌های بزرگ جواب نمی‌دهد؛ باید `source_paths` را محدود کرد یا heap را بالا برد.


---

## 🗺 SkillTree / «۱۳۷ ایجنت» — `skilltree.altari.ai` (بررسی ۲۰ اکتبر ۲۰۲۶، ریلز @reza…)

- **ریلز چه می‌گفت (از صدا):** ۱۳۷ ایجنت AI در ۷ دپارتمان (مارکتینگ، فروش، مالی...) که «کل شرکت را اداره می‌کنند»؛ اطلاعات کسب‌وکار را می‌گیرد و کارها را خودکار انجام می‌دهد؛ «دیگر لازم نیست خودت کاری بکنی»؛ بخشی رایگان. CTA: کامنت «۲۷» برای لینک.
- **واقعاً چیست:** محصول **SkillTree** از Altari — یک بستهٔ $۴۹/ماه از **فایل‌های ایجنت برای Claude** (۱۳۷ عنوان شغلی در ۷ دپارتمان) + یک «مصاحبهٔ آنبوردینگ» که Claude با آن knowledge base می‌سازد + audit engine. هنوز waitlist است، «۲٬۴۰۰ اپراتور» و ۱۰۰ صندلی مؤسس.
- **حکم:** **نیمه‌واقعی.** هر ایجنت یک فایل/پرامپت قابل اجراست، نه یک کارمند مستقل. خود سایت بعضی ایجنت‌ها را «in development» علامت زده و در ریزنویس، «کاملاً خودکار» یعنی یک انسان هر توالی ایمیل را تأیید می‌کند.
- **یعنی چه:** این یک «نقشهٔ شغل‌ها» است، نه شرکتی که خودش کار می‌کند. ارزش واقعی‌اش در چارچوب‌بندی و فایل‌های آماده است، نه در ادعای ریلز.
- **برای ما:** ما همین حالا ۲۸۲ متخصص در `agency-agents-router` و ۱۰۰+ مهارت داریم؛ $۴۹ برای فایل‌های پرامپت لازم نیست. ایدهٔ قابل‌برداشت: نقشهٔ ۷ دپارتمانی به‌عنوان دارایی فروش به مشتری (audit به‌عنوان پیشنهاد).


---

## 🪁 WatTunnel — `github.com/JohnWatsoon/WatTunnel` (بررسی ۲۰ اکتبر ۲۰۲۶، فوروارد تلگرام + بررسی API گیت‌هاب)

- **فوروارد چه می‌گفت:** تونل متن‌باز Go برای شبکه‌های محدود که «وقتی فقط ICMP رد می‌شود» کار می‌کند؛ ۹ روش انتقال (ICMP/TCP/UDP/Cloudflare+ECH)، انتخاب خودکار مسیر، ChaCha20-Poly1305، بازیابی خودکار؛ بنچمارک ICMP ~۳۳ MB/s.
- **واقعی است:** مخزن هست — ۶۶ ستاره، ۷ فورک، **MIT**، Go، **۶۶ فایل Go با تست** (~۱ MB کد)، ۳۰۳ کامیت، v2.5.1 (۱۶ اکتبر)، CI + `install.sh` با بررسی sha256.
- ⚠️ **پرچم‌های زرد:** ساخته‌شده ۱۰ اکتبر ۲۰۲۶ (≈۱۰ روز)، **تک‌نویسنده**، صفر اودیت مستقل، همهٔ بنچمارک‌ها self-reported (۳۳ MB/s روی ICMP در برابر ~۰.۵ MB/s برای pingtunnel بعید ولی ناممکن نیست).
- **نصب:** روی **دو سرور** (ایران + خارج) با root و systemd؛ `bash <(curl -fsSL .../install.sh)` باینری را از GitHub Releases می‌آورد. فقط زیرساخت است — کلاینت VPN نیست، جلویش Xray/VLESS لازم است.
- **کاربرد برای ما:** فعلاً هیچ (نیاز به سرور ایران + خارج دارد و درآمد مستقیم نمی‌سازد). اگر روزی سرور ایران داشتیم، ارزش تست در برابر GOST/Hans را دارد.


---

## 🧾 KYE-Protocol/schemas — `github.com/KYE-Protocol/schemas` (بررسی ۲۰ اکتبر ۲۰۲۶)

- **چیستی:** آینهٔ عمومی JSON Schemaهای پروتکل KYE برای «اثبات اختیار ایجنت در لحظهٔ اقدام»: موجودیت‌ها، تفویض، تصمیم، بستهٔ شواهد، replay proof، attestation و لایهٔ پرداخت. Apache-2.0، ساخت اوت ۲۰۲۶.
- **واقعیت مخزن:** **۱ ستاره، ۰ فورک، ۱ مشارکت‌کننده**، بدون زبان (فقط schema). یعنی یک اسپکِ شرکتی تازه، نه پروژهٔ جاافتاده.
- ⚠️ **نکتهٔ اصلی که خودشان نوشته‌اند:** schema فقط «شکل» را تعریف می‌کند؛ **مکانیزم** (چطور امتیاز حساب می‌شود، چطور bundle کانونیک می‌شود، آستانه‌ها چطور به نتیجه می‌رسند) «عامدانه و همیشگی» منتشر نمی‌شود. پس بدون vendor نمی‌شود صحتش را سنجید.
- ✅ **چیز قابل‌برداشت:** ایدهٔ Evidence Pack — هر ادعا همراه با ارجاع امضاشده به شواهد. پیاده‌سازی سبکش را در `workspace/ai-workforce-map/evidence_pack.py` ساختیم (SHA-256 + actors + limitations، بدون ادعای امضای دیجیتال).

## 🌐 x1cen/injspoof — `github.com/x1cen/injspoof` (بررسی ۲۰ اکتبر ۲۰۲۶)

- **چیستی:** تونل L2 با C + مسیر سریع XDP/AF_XDP؛ UDP محلی را در فریم خام اترنت با **IP مبدأ جعلی از استخر** می‌پیچد و به peer می‌فرستد؛ ظاهر ترافیک را TCP/UDP/ICMP جا می‌زند؛ ادعای میلیون‌ها فلوی همزمان.
- **واقعیت مخزن:** ۴ ستاره، MIT، آخرین پوش ژوئن ۲۰۲۶، یک نویسنده. کد Cِ کم‌ستاره که با `CAP_NET_RAW` روی روت اجرا می‌شود.
- ⛔ **تصمیم: نصب نمی‌کنیم.** جعل IP مبدأ + استتار پروتکل، ابزار استاندارد بازتاب/تقویت DDoS و دور زدن فیلتر است؛ روی سرور ما یعنی ریسک حقوقی و اخراج از هاست. حتی از نظر فنی هم پاسخ‌ها برنمی‌گردند مگر با دستکاری فایروال میزبان.
- **اگر هدف دور زدن سانسور است:** مسیر درست Xray/REALITY روی VPS است (مهارت `censorship-circumvention`)، نه جعل IP.


---

## 🎬 Dola AI — `dolai.video` (بررسی ۲۰ اکتبر ۲۰۲۶، ریلز)

- **ریلز چه می‌گفت (از صدا):** «دیگر برای ساخت ویدیو پول نده؛ این سایت رایگان ویدیوهایی می‌سازد که ابزارهای پولی هم نمی‌توانند.» مراحل: در گوگل «Dola AI» را بزن → حساب بساز (رایگان) → در بخش ویدیو تنظیمات را انتخاب کن → پرامپت بنویس (مثال: بچه‌ای در جنگل بازی می‌کند و پرواز می‌کند) → چند ثانیه صبر → ویدیو آماده. قابلیت دیگر: اول عکس بساز، بعد همان را به ویدیو تبدیل کن.
- **واقعی است:** `dolai.video` — مولد ویدیوی متنی/تصویری با کردیت روزانهٔ رایگان، کلیپ ۸–۱۵ ثانیه، نسبت‌های ۱۶:۹/۹:۱۶/۱:۱ و…، مدل‌های نسل جدید (Seedance/Veo) و قالب‌های UGC/Try-on.
- ⚠️ **«رایگان» یعنی فریمیوم:** پلن Basic $۱۹٫۹/ماه (۸۰۰ کردیت، ~۴۰ ویدیو)، Pro $۳۹٫۹ (۲۰۰۰ کردیت)، Enterprise $۹۹٫۹ (۶۰۰۰ کردیت).
- ⚠️ **تلهٔ مهم برای ما:** **لایسنس استفادهٔ تجاری فقط در پلن Enterprise** ذکر شده. یعنی ویدیوی ساخته‌شده در پلن رایگان/Basic برای کانال درآمدی DOPEAK ریسک حقوقی دارد.
- **کاربرد بالقوه:** فقط برای تست ایده و b-roll؛ برای انتشار در کانال، یا Enterprise لازم است یا باید با ابزار دارای مجوز تجاری صریح کار کنیم.


---

## 🛡 WhiteDNS / Soar-Server — `github.com/WhiteDNS/WhiteDNS-Android` (بررسی ۲۱ اکتبر ۲۰۲۶، فوروارد کانال WhiteDNS)

- **پست چه می‌گفت:** آماده‌سازی سرورهای عمومی WhiteDNS برای شرایط اضطراری؛ اپ از MasterDNS، CottonDNS، StormDNS و SOAR پشتیبانی می‌کند؛ برای iOS اپ CoreForge؛ سرور شخصی با پنل Soar-Server.
- **واقعی است:** `WhiteDNS-Android` — ★۱٬۳۹۸، ۹۷ فورک، Kotlin، آخرین نسخه **1.6.8**، آخرین پوش ۲۱ اکتبر ۲۰۲۶ (فعال). `Soar-Server` — Apache-2.0، Go، ★۴۸، ساخته ۱۷ اکتبر ۲۰۲۶ (تازه).
- ⚠️ **لایسنس:** source-available **proprietary** (کد باز برای شفافیت، ولی فورک/ری‌پک/انتشار مجدد ممنوع). در Play Store نیست — هر نسخهٔ آنجا غیررسمی است. کانال رسمی: `t.me/whitedns`.
- **محدودیت اصلی:** ابزار «اضطراری» است نه VPN — سرعت پایین، فقط وقتی پورت ۵۳ باز است.
- **سرور شخصی:** Ubuntu 22.04/24.04/26.04 یا Debian 12/13 (amd64)، root+systemd، **UDP/53 و TCP/53 باز**، **دامنه با NS delegation** (رکورد A برای nameserver + رکورد NS برای ساب‌دامین). نصب: `bash <(curl -fsSL https://raw.githubusercontent.com/WhiteDNS/Soar-Server/main/panel-setup.sh)`
- **ویدیوی آموزشی:** «WhiteDNS: نکات مهم برای اتصال سریع و مطمئن» — ۳۱:۴۹، ۷٬۶۴۰ بازدید، ۲۴ ژوئیه ۲۰۲۶.
- **کاربرد برای ما:** فقط سمت سرور ارزش دارد (اگر روزی VPS + دامنه داشتیم، تونل DNS به‌عنوان پلن B). سرورهای عمومی = فقط تست.


---

## 🖥 WProxy — GitHub: `Aliazadi-1776/WProxy-v2ray` (کلاینت دسکتاپ Xray/V2Ray)

- **چیستی:** کلاینت **دسکتاپ** برای لینوکس (GNOME 45–51 · KDE Plasma 6) و ویندوز ۱۰/۱۱. پایتون، **MIT**، v2.5.1 (۱۰ اکتبر ۲۰۲۶). مخزن: ۲۳ سپتامبر ۲۰۲۶ ساخته شده، **۵ ستاره، ۰ فورک**، توسعه‌دهندهٔ تنها.
- **چه می‌کند:** ایمپورت لینک VLESS / VMess / Trojan / Shadowsocks و سابسکریپشن HTTP(S)، اجرای Xray روی **TUN**، split routing، پینگ، مدیریت از Quick Settings گنوم / plasmoid KDE / tray ویندوز، و CLI.
- **بررسی کد (۲۲ اکتبر ۲۰۲۶، clone کامل):** مخزن واقعی و مهندسی‌شده (CI، docs، changelog). **تلمتری پیدا نشد.** روی لینوکس خود Xray را همراه ندارد؛ `scripts/install.sh` آن را از اسکریپت رسمی `XTLS/Xray-install` نصب می‌کند و بعد `xray.service` سیستم را خاموش می‌کند چون خودش Xray را اجرا می‌کند.
- ⚠️ **ریسک‌ها:** (۱) پروژهٔ بسیار تازه با کاربر کم — کد MIT و قابل بازبینی، ولی هنوز آزمون زمان نداده. (۲) نصب‌کنندهٔ ویندوز `Setup.exe` **امضای کد (code signing) ندارد** و Xray + Wintun را داخل خود دارد → SmartScreen و بعضی آنتی‌ویروس‌ها گیر می‌دهند. (۳) روی لینوکس root + systemd + NetworkManager لازم است.
- ❌ **macOS ندارد.** اسکرین‌شات V2RayX 2.2.10 که فرستاده شد کلاینت دیگری است و ربطی به WProxy ندارد.
- **توصیه:** روی ویندوز **v2rayN** بالغ‌تر و شناخته‌شده‌تر است؛ WProxy فقط وقتی معنی دارد که ادغام Quick Settings گنوم/پلاسما را بخواهی. لینک VLESS+REALITY خودمان (`workspace/xray-config/vless-link-80.txt`) در هر سهٔ این‌ها مستقیم ایمپورت می‌شود.


---

## 📱 MLM VPN — GitHub: `mlmvpn/mlmvpn_android` + `mlmvpn/mlmvpn_windows` (چندموتوره، واقعاً فعال)

- **چیستی:** دو اپ جدا از یک توسعه‌دهنده. **اندروید:** Kotlin + Jetpack Compose، **GPLv3 + شرط ارجاع**، minSdk 24 — Xray (VLESS/VMess/Trojan با REALITY/WS/gRPC) + AmneziaWG + SoftEther + WARP + Psiphon + Tor + Geph + Aether (MASQUE) + OpenVPN + اسکنر نود + پنل Cloudflare. **ویندوز:** Electron 42، ۱۴ موتور، اسکنر IP تمیز، split routing هر اپ، kill switch، DNS guard؛ لایسنس اختصاصی «MLMVPN Attribution» (نه OSI).
- **وضعیت واقعی (۲۲ اکتبر ۲۰۲۶):** اندروید **۴۴۷ ستاره / ۸۳ فورک**، آخرین نسخه **v1.2.42** (۲۰ اکتبر) — APK arm64 ‏۱۴۳MB با **۱۸٫۱ هزار دانلود**. ویندوز **۲۹۲ ستاره**، نسخهٔ **1.2.6** (۲۰ اکتبر) — Setup x64 ‏۲۸۱MB با ۲٫۳ هزار دانلود. هر دو فعال و در حال توسعه.
- **چه چیزی ثابت می‌کند جدی است:** سورس کامل + بیلد از سورس، ریلیزهای منظم هفتگی، حجم دانلود واقعی، پشتیبانی از REALITY (چیزی که اپ‌های تقلبی ندارند).
- **ادعای حریم خصوصی:** «هیچ سرور MLMVPN در مسیر داده نیست» — ترافیک از نود خودت یا شبکه‌های عمومی (WARP/Psiphon/Tor/Geph/VPN Gate) می‌رود. با سورس سازگار است، ولی تأیید مستقل نشده.
- ⚠️ **ریسک‌ها:** (۱) در Play Store نیست → sideload با «نصب از منابع ناشناس» و بدون بازبینی Play Protect. (۲) موتورهای عمومی = خروجیِ شخص ثالث → برای بانک/لاگین نه. (۳) اینستالر ویندوز امضا ندارد و ۲۸۱MB است (۱۴ موتور داخلش) → SmartScreen گیر می‌دهد، طبیعی است. (۴) اسکرین‌شات‌های URnetwork و «سیاقون» که فرستاده شد **اپ‌های دیگری** هستند و ربطی به MLM ندارند.
- **کاربرد برای ما:** لینک `vless://` خودمان را در تب Nodes ایمپورت می‌کند و با موتور Xray کار می‌کند؛ اسکنر IP برای نودهای CDN عمومی است، نه برای رفع SNI غلط.
- 📚 دانش کامل + روش نصب/ایمپورت در مهارت `mlmvpn` ذخیره شد.

---

## 🗄️ drawDB — GitHub: `drawdb-io/drawdb` (واقعی، ۲۲ اکتبر ۲۰۲۶)

- **چیستی:** ادیتور بصری ERD و SQL generator تحت وب؛ کل ادیتور در مرورگر، بدون ثبت‌نام.
- **اعداد واقعی (GitHub API، ۲۲ اکتبر ۲۰۲۶):** ۴۰٫۱k ستاره، ۳٫۳k فورک، ۲۴۷ issue باز، لایسنس **AGPL-3.0**، زبان JavaScript، آخرین push ۱۵ اکتبر → فعال.
- **ادعاهای ریل و درستی‌شان:** «رایگان/اوپن‌سورس» ✅ | «بدون ثبت‌نام» ✅ | «export SQL یک‌کلیکی» ✅ | «reverse engineer» ✅ ولی **از فایل DDL**، نه اتصال زنده به دیتابیس.
- **دیالکت‌ها:** MySQL, PostgreSQL, SQLite, MariaDB, SQL Server, Oracle + generic؛ export به SQL / DBML / JSON / تصویر.
- **چیزهایی که ریل نمی‌گوید:** (۱) در نسخهٔ رایگان دیاگرام‌ها در **IndexedDB مرورگر** ذخیره می‌شوند — پاک‌کردن کش مرورگر = از دست رفتن کار. (۲) AI assistant، همکاری real-time، cloud sync و teams = **پلن Pro پولی**. (۳) AGPL یعنی اگر تغییرش بدهیم و به‌صورت سرویس شبکه‌ای بدهیم باید سورس را منتشر کنیم (استفادهٔ داخلی/ابزاری آزاد است). (۴) کامنت «DRAWDB» صرفاً قیف مارکتینگ است.
- **کاربرد برای ما:** برای طراحی سریع اسکیمای دیتابیس هر پروژه (SaaS/ربات/داشبورد) و گرفتن DDL آماده؛ self-host با یک دستور Docker. خودش محصول درآمدزا نیست — ابزار سرعت است.

## ElevenLabs — کلون صدا (ریل @ai.creator / DfFWFKrN2sn، ۳۰ اکتبر ۲۰۲۶)

- **محصول:** واقعی. ElevenLabs (elevenlabs.io). کلون فوری صدا (Instant Voice Cloning) واقعاً هست: ۱–۳ دقیقه نمونه صدا → صدای کلون‌شده.
- **ادعای ریل:** «این صدای منه و خودم ضبطش نکردم، توی 11 Labs کلونش کردم» — **قابل راستی‌آزمایی نیست**؛ هر صدایی (حتی صدای پیش‌فرض یا شخص دیگر) را می‌شود زیر این ادعا گذاشت. خودِ قابلیت اما واقعی است.
- **قیمت واقعی (صفحهٔ pricing، ۳۰ اکتبر ۲۰۲۶):** Free = ۰ دلار، ۱۰٬۰۰۰ کردیت، **بدون لایسنس تجاری** (فقط با attribution)؛ Starter = ۶ دلار (۳۰٬۰۰۰ کردیت، شامل لایسنس تجاری)؛ Creator = ۲۲ دلار (۱۲۱٬۰۰۰ کردیت + Professional Voice Cloning)؛ Pro = ۹۹ دلار (۶۰۰٬۰۰۰).
- **Instant Cloning از کدام پلن:** Starter و بالاتر. یعنی «رایگان» در عمل وجود ندارد اگر پول درآوردن هدف باشد.
- **قابلیت‌هایی که ریل نمی‌گوید:** لایسنس تجاری فقط از پلن پولی؛ رضایت صوتی برای کلون لازم است؛ کیفیت فارسی/آلمانی خوب ولی با لهجهٔ گویندهٔ مرجع.
- **مدل درآمدی ریل:** قیف تلگرام — «کامنت کن الون» + «آموزش کامل در کانال تلگرام». خود ElevenLabs محصول جانبی است.

### محاسبهٔ ما
- اسکریپت شورت DOPEAK ≈ ۱۲۰ کلمه ≈ ۷۵۰ کاراکتر → ۳۰٬۰۰۰ کردیت ≈ **۳۸–۴۰ شورت در ماه** یا ~۳ ویدیوی لانگفرم ۱۰ دقیقه‌ای.
- **اما:** صدای کلون‌شده لهجهٔ B2 احمد را به ارث می‌برد. برای مخاطب آلمانی/انگلیسی، صدای نیتیو فعلی edge-tts بهتر است. کلون فقط وقتی برنده است که «صدای خودِ سازنده» بخشی از برند باشد — که برای DOPEAK (فیس‌لس) نیست.
- **حکم:** ابزار واقعی و ارزان، ولی برای پایپ‌لاین فعلی ما بدون سود. اگر روزی کانال فارسی/شخصی‌محور راه بیفتد، Starter با ۶ دلار انتخاب اول است.

---

## 2026-11-02 — InviZible Pro (Gedsh/InviZible)

- **وضعیت:** واقعی و فعال. GPL-3.0، Java، ۲٬۸۶۳ ستاره، ۱۷۲ فورک، ۹۷ مشارکت‌کننده. آخرین انتشار `v7.6.0-stable` در ۲۷ اکتبر ۲۰۲۶؛ آخرین کامیت ۳۰ اکتبر ۲۰۲۶.
- **چی هست:** اپ اندروید که Tor + DNSCrypt + Purple I2P را در یک VPN سیستم‌wide ترکیب می‌کند. مسدودسازی تبلیغ/بدافزار از طریق سرور DNSCrypt، دسترسی به onion و eepsite.
- **هشدار تبلیغ:** «گمنامی کامل» ادعای بازاریابی است، نه واقعیت. APKهای صفحه Releases نسخه **Lite** هستند، نه Pro؛ Pro روی Play و F-Droid است.
- **حکم برای ما:** برای دور زدن فیلترینگ در ایران ضعیف‌تر از Xray/REALITY خودمان است (Tor در ایران به‌شدت بلاک است). ارزش واقعی‌اش: بلاک تبلیغ + دسترسی onion. برای گوشی احمد گزینه جانبی است، نه جایگزین.

## 2026-11-02 — chigwell/telegram-mcp

- **وضعیت:** واقعی و فعال. Apache-2.0، Python، ۱٬۹۵۸ ستاره، ۴۸۹ فورک. آخرین کامیت ۳۱ اکتبر ۲۰۲۶.
- **چی هست:** سرور MCP روی Telethon با **اکانت شخصی** (نه بات). **۳۴۵ ابزار** (تبلیغ «۸۰+» گفته بود — کم گفته): خواندن/جست‌وجوی چت، ارسال و ویرایش، مدیریت گروه و ادمین، مخاطبین، رسانه، ویس به متن، Business.
- **ریسک:** با سشن اکانت شخصی کار می‌کند → هر ایجنتِ وصل‌شده می‌تواند به‌جای احمد پیام بفرستد، و اتوماسیون روی اکانت کاربر خلاف ToS تلگرام است (ریسک بن).
- **وضعیت محلی:** ریپو در `workspace/telegram-mcp` کلون شده، `.env` با API_ID/HASH/SESSION_STRING موجود، `TELEGRAM_EXPOSED_TOOLS=read-only`. در `mcp_servers` هرمس ثبت نشده و telethon در venv نصب نیست → فعلاً وصل نیست.

---

## 📦 فورواردهای ۳ نوامبر ۲۰۲۶ (RepoFA / اینستاگرام)

### 🖥️ TwinDesk — `inukaasith/twindesk`
- **چیستی:** اشتراک «میز» بین چند دستگاه: ماوس و کیبورد، کلیپ‌بورد، فایل، نوتیفیکیشن و پیام، بین Mac / Windows / Linux / Android. بدون اکانت، بدون کلود، و طبق ادعای خودش بدون نیاز به شبکهٔ مشترک.
- **آمار واقعی:** **۳٬۲۱۹ ستاره** · ۲۴۰ فورک · ۳۱ ایشوی باز · GPL-3.0 · ساختهٔ ۱۴ اکتبر ۲۰۲۶ · آخرین پوش ۳ نوامبر ۲۰۲۶ (فعال) · JavaScript · ۱۳MB.
- **وضعیت:** واقعی و زنده است، نه پروژهٔ مرده.
- **کاربرد برای ما:** ❌ هیچ. این یک لایهٔ **KVM برای انسان** است (ماوس/کیبورد بین دو نمایشگر)، روی سرور headless کاری نمی‌کند و ایجنت را به ایجنت وصل نمی‌کند. برای خود احمد بین لپ‌تاپ و PC ابزار خوبی است.
- **لینک:** https://github.com/inukaasith/twindesk

### 🧠 FloMorphic — `FloMorphic/getting-started`
- **چیستی:** پلتفرم کم‌کد ساخت ایجنت روی زیرساخت خودی: گراف اجرایی با کانتکست مشترک، MCP بومی، ابزار RAG، حافظهٔ پایدار، هماهنگی چندایجنتی و نظارت انسانی؛ ادعای استقرار از لپ‌تاپ تا کلاستر.
- **آمار واقعی:** ریپوی `getting-started` فقط **۱ ستاره** · Apache-2.0 · Shell · ساختهٔ ۲۵ ژوئیه ۲۰۲۶. کل سازمان: ۸ ریپو، همه **۰ تا ۱ ستاره** · سایت تجاری `inflowenger.com/flomorphic`.
- **وضعیت:** وجود دارد، ولی هیچ پذیرشی ندارد — «پروداکت در حال فروش»، نه پروژهٔ اجتماعی.
- **کاربرد برای ما:** ❌ فعلاً نه. ما همین حالا یک کنترل‌پلین داریم (Hermes + ۳۱۴ اسکیل ECC + ۲۸۲ متخصص The Agency)؛ اضافه‌کردن یک گراف‌اجراکنندهٔ دوم یعنی دو مغز موازی و دو جای حقیقت. تنها ایدهٔ قابل قرض‌گرفتن: «گراف اجرایی + ردپای ممیزی‌پذیر» که در `ecc-orch-pipeline` تقریباً معادلش را داریم.
- **لینک:** https://github.com/FloMorphic/getting-started

### 🌐 TWP-CF — `MHDLabs/TWP-CF`
- **چیستی:** پروکسی وب تلگرام روی Cloudflare Workers: `client → HTTPS → Worker → WebSocket → Durable Object → TCP → Telegram DC`. یک کلیک دیپلوی با Workers.
- **آمار واقعی:** **۱۱ ستاره** · ۹ فورک · JavaScript · ۶۴KB · ساخته ۹ اکتبر ۲۰۲۶، آخرین پوش **۱۰ اکتبر ۲۰۲۶** (تک‌روزه، مرده). لایسنس: سفارشی (گیت‌هاب `NOASSERTION`)، استفادهٔ آزاد با ذکر ریپوی اصلی.
- **⚠️ ریسک:** پروکسی یعنی ترافیک MTProto تو از سرور یه نفر دیگر رد می‌شود. **هرگز با اکانت اصلی داخل یک پروکسی شخص ثالث لاگین نکن** — نشست و شماره در معرض است. خود README هم هشدار داده که با اختلالات اینترنت ایران پایدار نیست.
- **کاربرد برای ما:** ❌ برای دور زدن فیلتر، مسیر خودمان (Xray/REALITY در `g2ray`) امن‌تر و تحت کنترل خودمان است. اگر فقط دسترسی «تلگرام وب» در مرورگر می‌خواهی، دیپلوی شخصی روی اکانت کلادفلر خودت قابل قبول است (کلیدش را خودت داری).
- **لینک:** https://github.com/MHDLabs/TWP-CF

### 🌳 tree-of-neuron — `fermow/tree-of-neuron`
- **چیستی:** تاریخ تعاملی کشف نورون: ۴۷ نقطهٔ عطف در یک درخت پژوهشی با شش مسیر موازی، هر گره = داستان + شواهد آزمایشگاهی + محدودیت‌ها + مقالات لینک‌شده. بدون build؛ HTML/CSS/SVG/JS خالص.
- **آمار واقعی:** **۱ ستاره** · ۰ فورک · **بدون هیچ لایسنس** · ۲۵۲KB · ساخته ۹ اکتبر ۲۰۲۶، پوش ۱۵ اکتبر. سایت زنده: https://fermow.github.io/tree-of-neuron/ (۲۰۰ ✓).
- **وضعیت:** محتوایش جدی و منبع‌دار به نظر می‌رسد، ولی «بدون لایسنس» یعنی از نظر حقوقی هیچ اجازه‌ای برای بازاستفاده نمی‌دهد.
- **کاربرد برای ما:** ❌ آموزشی/تزئینی، نه ابزار. تنها چیزی که ارزش کپی دارد، **الگوی ارائه** است: تایم‌لاین درختی + پنل شاهد + منبع برای هر گره — همان چیزی که برای پورتفولیو یا محتوای آموزشی خودمان قابل استفاده است (باید از صفر خودمان بسازیم، نه کپی).
- **لینک:** https://github.com/fermow/tree-of-neuron

### 🎬 مجموعهٔ «۹ اسکیل انیمیشن کلود» (کاروسل @okaashish، ۲ نوامبر ۲۰۲۶)
خلاصهٔ بررسی: هر ۹ مورد به ریپوهای واقعی وصل‌اند، ولی کیفیتشان زمین تا آسمان فرق دارد.

| نام در پست | ریپوی واقعی | ستاره | لایسنس | حکم |
|---|---|---|---|---|
| Huashu Art Motion | `alchaincyf/huashu-art-motion` | ۶٬۰۵۱ | MIT | ✅ بهترین گزینه: ۳۵ سبک + ۹ گرامر توضیحی، خروجی MP4 |
| Huashu Design (خانواده) | `alchaincyf/huashu-design` | ۲۸٬۵۳۱ | MIT | ✅ پلتفرم طراحی HTML→PPTX/تیزر |
| Anidoodle | `alexgreensh/anidoodle` | ۱٬۲۳۷ | Apache-2.0 | ✅ ۳۲ سبک که با کد کشیده می‌شوند، plugin برای Claude/Codex |
| Motion Design Skill | `LottieFiles/motion-design-skill` | ۲٬۷۵۴ | MIT | ⚪ فقط قواعد timing/easing، بدون کد |
| Claude Animation Base | `JohnHeibel/ClaudeAnimationBase` | ۲٬۵۱۲ | MIT | ⚪ p5.js؛ روی CPU کند |
| Claude Animation | `buildwithhanif/claude-animation-skill` | ۱۱۹ | MIT | ⚪ نیاز به node+ffmpeg |
| Handdraw Skill | `ToBeWin/HandDraw-Skill` | ۱۲ | MIT | ⚪ وایت‌برد + نریشن Edge TTS + زیرنویس؛ جالب ولی نو |
| Motion Skill (Nano Banana + Kling) | — | — | — | ❌ پولی/API، روی سرور ما ممکن نیست |
| Manim Skill | `ManimCommunity/manim` | — | MIT | ✅ از قبل داریم (`manim-video`) |

- **⚠️ محدودیت سخت‌افزاری (اندازه‌گیری‌شده):** رندر آبرنگی p5.brush روی CPU بدون GPU حدود **۴۰ ثانیه برای هر فریم** است؛ یک فیلم ۱۱ ثانیه‌ای ≈ ۳ ساعت. مسیرهای HTML→MP4 و Manim روی CPU قابل تحمل‌اند، مسیرهای مرورگری/آبرنگی نه.
- **مسیرهای ما که همین حالا همین کار را می‌کنند:** `manim-video` · `motion-graphics-films` (HTML→MP4) · `p5js` · `threejs-interactive-demo`.

### 🤖 Muse (متا) — از سؤال «اوپن‌سورسه؟ لوکال می‌شه؟»
- **Muse = خانوادهٔ متا:** اپ/ایجنت Muse (آمریکا + سنگاپور) · مدل‌های **Muse Spark** (1.3) · **Muse Wonder / Wonder Full** · **Muse Image** و **Muse Video** (پیش‌نمایش).
- **Muse Spark Open** — وزن باز ولی **نه اوپن‌سورس**: ۸۱۶B کل / ۴۲B فعال، کانتکست ۱M، لایسنس «Muse Model License» با شروط تجاری محدود. کوچک‌ترین کوانت (IQ1_M) = **۲۰۹GB** → روی هیچ ماشین ما معنا ندارد.
- **Muse Glimmer 30B** — این یکی واقعاً اوپن‌سورس است: **Apache-2.0**، ۲۹٫۸B، مالتی‌مودال. روی `ki` نصب شد و اندازه‌گیری شد: **۲٫۰۶ توکن/ثانیه** تولید، ۸٫۴ توکن/ثانیه پرامپت، ۱۳GB رم با کانتکست ۸k. جزئیات: `workspace/remote-ki/glimmer.md`.
- **روی OpenRouter:** `meta/muse-spark-1.3` (۱٫۲۵$/۴٫۲۵$ به میلیون) · `meta/muse-spark-1.3-contributor` (۰٫۱$/۰٫۲$) · `meta/muse-wonder` (۴$/۲۰$) · `meta/muse-glimmer-30b` (۰٫۳$/۱٫۲$).
- **حکم:** برای کار روزمرهٔ ما deepseek/groq ارزان‌تر است؛ ارزش Spark کانتکست ۱M برای «کل ریپو را بخوان» است.

### 🧰 ECC — `affaan-m/ECC` (از ریلز @moeen_valpr)
- **آمار تأییدشده (۲ نوامبر ۲۰۲۶):** **۲۹۵٬۶۲۳ ستاره** · MIT · ۳۱۴ اسکیل · ۷۱ ایجنت · ۹۸ کامند · v2.2.3 · کامیت `b38be6a`.
- **نصب‌شده برای ما:** آینهٔ کامل در `workspace/ecc` + کاتالوگ در `workspace/ecc-index` + مهارت `ecc-toolkit` + ۱۲ اسکیل ایمپورت‌شده در `skills/ecc/`.
- **انتشار عمومی خودمان:** `github.com/ahmadvahidi/skill-atlas` — ۴۰ اسکیل منتخب با تصاویر تولیدشده و مستندات (MIT + NOTICE).
- **حکم:** تنها موردی از این فورواردها که واقعاً به گردش کارمان اضافه شد.

### 🎬 Code Animation Prompts — `XiaoyeCodes/code-animation-prompts` (ریل @Github Signals، ۳ نوامبر ۲۰۲۶)
- **چیستی:** کتابخانهٔ **۳۴۱ سبک انیمیشن** که با کد ساخته می‌شوند؛ هر سبک یک پرامپت + «چه شکلی است» + «برای چه حسی مناسب است» + کلیدواژه. **۲۹ سبک** کد اجرایی Canvas 2D هم دارند.
- **آمار واقعی:** ۳۸۹ ستاره · لایسنس سفارشی «اشتراک آزاد» (نه MIT) · ۸۰MB (شامل ۱۹۳ استیل) · ساخته و پوش‌شده در **۲۹ اکتبر ۲۰۲۶** (یک‌روزه — محتوا واقعی، نگهداری نه).
- **لایسنس — مهم:** استفاده و بازنشر آزاد، ولی **فروش یا بسته‌بندی به‌عنوان محصول/دوره ممنوع**؛ ذکر منبع لازم است.
- **چی برای ما شد:** آینهٔ آفلاین کامل در `workspace/animation-styles/` — ۳۴۱ فایل پرامپت (۲٫۶MB)، `INDEX.md` گروه‌بندی‌شده، و رندر headless با `render_style.py` (بدون playwright/node). مهارت `code-animation-styles` ساخته شد.
- **تست واقعی:** سبک **B5** (دایرهٔ نفس‌کش) → ۳۶ فریم ۴۸۰×۸۵۴ → `preview_b5.mp4` (۳ ثانیه، ۱۰۹KB) ✓ رندر شد و با vision تأیید شد که فریم واقعی است نه سیاه.
- **عیب شناخته‌شده:** فونت چینی روی این جعبه نیست → متن‌های CJK در فریم‌ها مربع خالی می‌شوند (در B5 دیده شد).
- **کاربرد:** انتخاب «حس بصری» برای شورت/اینترو/دیتاویژوال؛ ۳۱۲ سبک دیگر فقط جهت‌گیری خلاقانه‌اند نه کد آماده.

---

## 🕓 پارک‌شده برای بعد (یاد گرفتیم، الان استفاده نمی‌کنیم)

### 🎭 RGB MoCap — `toyxyz/toyxyz_rgbmocap` (ریل @Github Signals، ۴ نوامبر ۲۰۲۶)
- **چیستی:** اپ نیتیو ویندوز که **ویدیوی معمولی را به انیمیشن سه‌بعدی قابل‌ویرایش** تبدیل می‌کند: موشن‌کپچر با ExMR / FlowHMR / GVHMR، اصلاح پاهای سُر‌خورنده (contact correction)، ریتارگت روی مدل کاراکتر، خروجی **FBX و VMD** برای موتور بازی و نرم‌افزار انیمه. همهٔ پردازش محلی، بدون کلود.
- **آمار واقعی:** **۵۹۶ ستاره** · ۷۹ فورک · MIT · Python · ۴۴MB · ساختهٔ ۲۶ اکتبر ۲۰۲۶، آخرین پوش ۳ نوامبر ۲۰۲۶ (فعال).
- **نیازمندی سخت:** ویندوز ۶۴بیتی + **GPU انویدیا** با درایور سازگار + OpenGL 4.3 + CUDA 12.8 برای بیلد نیتیو؛ Plus Blender، FFmpeg و دانلود جداگانهٔ وزن‌ها در Model Manager.
- **چرا الان نه:** سرور ما لینوکس است و GPU ندارد (`Capabilities: 0`, بدون `/dev/dri`). روی این جعبه حتی نصب نمی‌شود.
- **کِی سراغش برویم:** وقتی ریگ GPU (یا یک ویندوز با RTX) راه افتاد. اولین کاربرد واقعی: موشن‌کپچر از ویدیوی خودمان و ریتارگت روی کاراکتر برند DOPEAK — بدون استودیو و بدون بازیگر.
- **لینک:** https://github.com/toyxyz/toyxyz_rgbmocap

### 👻 Ghostman — `4yk5/ghostman` (ریل @Github Signals، ۴ نوامبر ۲۰۲۶)
- **چیستی:** کلاینت API و بازرس وبهوک، تماماً ترمینالی (TUI با Textual): درخواست HTTP بساز/بفرست، و با `Ctrl+W` یک شنوندهٔ وبهوک روی پورت ۹۰۹۰ بالا بیاور تا پیلودهای Stripe/GitHub را همانجا ببینی. بدون اکانت، بدون کلود؛ داده در `~/.ghostman/` بهصورت JSON/YAML.
- **آمار واقعی:** **۱۰۶ ستاره** · ۲ فورک · **MIT** · Python · ۳۶۴KB · ساخته ۳۰ اکتبر ۲۰۲۶، پوش ۳ نوامبر (تازه، ولی فعال). روی PyPI هم هست.
- **ادعاهای خودش:** بوت ~۱۵۰ms و ~۳۰MB رم در برابر ۸۰۰MB–۱٫۵GB پستمن؛ کلیدها: `Ctrl+S` ارسال، `Ctrl+K` ذخیره، `Ctrl+N` درخواست جدید.
- **کاربرد برای ما:** ✅ واقعی و سبک؛ برای تست وبهوکهای ربات تلگرام و GitHub و همین APIهای خودمان روی سرور بی‌نمایشگر مفید است — جای ngrok/webhook.site. هنوز نصب نشده (تصمیم با احمد).
- **لینک:** https://github.com/4yk5/ghostman

### 🛰️ Masque Config Generator — `DarknessShade/Masque-Generator` (فوروارد ۴ نوامبر ۲۰۲۶)
- **چیستی:** صفحهٔ وب تک‌فایلی که از یک رجیستریشن WARP، کانفیگ **MASQUE (CONNECT-IP, RFC 9484)** می‌سازد: لینک `masque://`، JSON، و پروفایل Clash / v2rayNG / Happ / Streisand. ادعای سازنده: H2 پیش‌فرض برای همراه اول، برای ایرانسل با endpoint و SNI بیشتر.
- **آمار واقعی:** **۱۴ ستاره** · MIT · ۲۷۱KB · ساخته و پوش ۳ نوامبر ۲۰۲۶ (یک‌روزه). دکمهٔ fallback به یک Cloudflare Worker جدا می‌رود: `masque-generator.configwireguard.workers.dev` (کانال تلگرام `@ConfigWireguard`).
- **فنی — درست است:** خود Xray از MASQUE پشتیبانی می‌کند (`protocol: masque` + `masqueSettings.warp` با کلید P-256؛ نه Curve25519 وگارد). MASQUE روی TCP/443 با ظاهر HTTPS کار می‌کند، یعنی جایی که UDP بلاک است (ایرانسل). کلید P-256 و آدرس‌ها از ثبت WARP می‌آیند و `warp_enabled` باید روشن باشد.
- **ریسک:** اگر کلید را در فرم بگذاری و ساخت سمت Worker انجام شود، اپراتور آن Worker کلید دستگاهت را می‌بیند (برای WARP یعنی می‌تواند از سهمیهٔ تو استفاده کند، نه اینکه ترافیک TLS را بخواند). بهتر: ساخت محلی با `warp-cli` یا `usque` (۱۵۱۴ ستاره، MIT) و همان کلید را در ژنراتور فقط برای قالب‌بندی بده.
- **کاربرد برای ما:** ✅ مسیر درست برای عبور از ایرانسل؛ ولی چون سرویس شخص ثالث یک‌روزه است، کلید را از منبع رسمی بگیر و فقط قالب را از این صفحه.
- **لینک:** https://github.com/DarknessShade/Masque-Generator · https://darknessshade.github.io/Masque-Generator/

---

## 📚 آرشیو فورواردها (به‌جای حافظه)

هر لیست/کاروسل «۱۰ ابزار رایگان» با بررسی تک‌تک در گیت‌هاب منتشر می‌شود تا حافظهٔ من سبک بماند:
- **`github.com/ahmadvahidi/open-source-alternatives`** — کاروسل ۳ نوامبر ۲۰۲۶ (@amirm_design): ۱۰ ابزار،
  با ستاره/لایسنس/پلتفرم واقعی و حکم برای استک ما. بازتولید جدول: `python3 tools/build.py --verify`.
- خلاصهٔ همان لیست: فقط **VoiceStudio** (کلون صدا، نیاز GPU) و **Cal.com** (رزرو جلسه، نیاز هاست+دامنه)
  به کار ما می‌آیند؛ بقیه GUI/دسکتاپ‌اند یا کاری را که با کد انجام می‌دهیم تکرار می‌کنند.

### 🧠 Weight-Space Programming (MIT CSAIL) — ادعای «۶ برابر ریاضی» (فوروارد ۴ نوامبر ۲۰۲۶)
- **ادعا:** GPT-6 Astra وزن‌های Qwen3.5-0.8B را مستقیم (بدون گرادیان/فاین‌تیون) ویرایش کرده، فقط **۰٫۰۱۶٪** وزن‌ها، و MATH-500 از ۷٫۹٪ به ۴۸٫۱٪ رسیده؛ IFEval هم ۳ برابر.
- **چیزهایی که واقعاً منتشر شده (بررسی شد):** بلاگ `rikiyat.github.io/blog/weight-space-programming` (۲ نوامبر ۲۰۲۶) · لاگ کامل `RikiyaT/lm_understand-logs` (**۸۴۳ ستاره**) · مدل ویرایش‌شده روی HF `RikiyaT/Qwen3.5-0.8B-weight-space-programming` (۱٬۲۹۷ دانلود، ۷۹ لایک) · دموی Space + فایل‌های ارزیابی.
- **⚠️ ایرادی که در خود فایل‌های ارزیابی پیدا کردم:** مقایسه هم‌شرط نیست. `scores_base_math500.json` → **۲۵ مسئله**، دقت ۰٫۰۵، و **۹۵٪ پاسخ‌ها در ۳۲k توکن بریده شده‌اند**؛ `scores_edited_math500.json` → **۵۰۰ مسئله**، دقت ۰٫۵۱، بریدگی ۳۱٫۶٪. یعنی «۶ برابر» حاصل مقایسهٔ یک بیس‌لاین کوچک و ناتمام با یک اجرای کامل ۵۰۰تایی است.
- **آنچه واقعاً ثابت می‌شود:** مدل پایه در حلقهٔ استدلال گیر می‌کرد و تمام نمی‌کرد؛ ویرایش وزن آن حلقه را باز کرده. این همان چیزی است که خودشان ادعا می‌کنند — ولی عدد ۶ برابر، ضریب تبلیغاتی است نه اندازه‌گیری کنترل‌شده.
- **کاربرد برای ما:** وقتی ریگ GPU آمد، این روش راه ارزانی است برای درست‌کردن مدل کوچک محلی بدون دیتاست. الان نه (نیاز به Astra که عمومی نیست).

### 🧱 StableGen — `sakalond/stablegen` (ریل @Github Signals، ۴ نوامبر ۲۰۲۶)
- **چیستی:** افزونهٔ Blender که از یک پرامپت، **مش + ریگ + تکسچر PBR** می‌سازد: TRELLIS.2 مش می‌سازد، SkinTokens ریگ می‌کند، Marigold نقشه‌های albedo/roughness/metallic/normal می‌دهد و همه را روی مش پروجکت می‌کند. خروجی قابل اکسپورت به Unity/Unreal.
- **آمار واقعی:** **۱٬۴۵۲ ستاره** · ۱۴۱ فورک · GPL-3.0 · Python · ساختهٔ مه ۲۰۲۵، آخرین پوش ۲ نوامبر ۲۰۲۶ (بالغ و فعال — نه دراپ یک‌روزه).
- **نیازمندی سخت:** Blender 4.2–4.5 / 5.1+ و یک سرور **ComfyUI** (محلی یا در شبکه) با مدل‌های diffusion. یعنی **GPU با VRAM قابل‌توجه**. روی این جعبه نه Blender هست نه GPU (`/dev/dri` وجود ندارد).
- **کاربرد برای ما:** کاراکتر برند DOPEAK (ماسکوت سه‌بعدی برای تامبنیل/شورت) — ولی فقط با GPU. گزینهٔ عملی قبل از خرید ریگ: یک ساعت GPU اجاره‌ای (RunPod/A4000) برای تولید یک دارایی، نه برای پایپ‌لاین.

### 🟦 ascii.rest — `bas3line/ascii` (ریل @animmaster_studio، ۴ نوامبر ۲۰۲۶)
- **چیستی:** کتابخانهٔ **۲۴۰ قطعهٔ ASCII متحرک** برای وب — از منظره و فضا تا لوگو و چارت. یک تگ ساده: `<ascii-art piece="donut"></ascii-art>`؛ نسخه‌های React، Next.js، Astro، یا HTML بدون build (`<script type="module" src="https://ascii.rest/ascii.js">`). تکه‌های رنگی روی canvas و تک‌رنگ‌ها داخل `<pre>` رندر می‌شوند.
- **آمار واقعی:** **۱٬۱۳۵ ستاره** · ۶۶ فورک · **MIT** · TypeScript · ساختهٔ ۷ اکتبر ۲۰۲۶، پوش ۳۰ اکتبر (تازه ولی فعال). سایت: `ascii.rest`، پکیج npm: `ascii.rest`، رجیستری shadcn هم دارد.
- **تست واقعی (۴ نوامبر):** صفحهٔ `workspace/ascii-rest-demo/index.html` با سه قطعه (`night-coast`، `earthrise`، `taj-dawn`) در chrome-headless رندر شد و هر سه صحنه کامل و رنگی بالا آمدند، بدون خطا ✓
- **ریل فرستاده‌شده** همان گالری/ادیتور همین پروژه است؛ «LIB» فقط کلیدواژهٔ کامنت برای لینک است، نه اسم کتابخانه.
- **کاربرد برای ما:** صفحهٔ فرود DOPEAK، سایت skill-atlas، بک‌گراند شورت‌ها و پنل‌های ترمینالی. سبک و MIT — قابل استفادهٔ مستقیم.
