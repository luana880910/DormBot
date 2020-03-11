import discord
from discord.ext import commands
import random
from core.classes import Cog_Extension

class LOLBot(Cog_Extension):

    
    @commands.command()
    async def 骰英雄(self,ctx):
        LOL_champion = ['厄薩斯','阿璃','阿卡莉','亞歷斯塔','阿姆姆','艾妮維亞','安妮','艾希','翱銳龍獸','阿祈爾','巴德','布里茨','布蘭德','布朗姆','凱特琳','卡蜜兒','卡莎碧雅 ','科加斯','庫奇','達瑞斯','黛安娜','達瑞文','蒙多醫生','艾克','伊莉絲','伊芙琳','伊澤瑞爾','費德提克','菲歐拉','飛斯','加里歐','剛普朗克','蓋倫','吶兒','古拉格斯','葛雷夫','赫克林','漢默丁格','伊羅旖','伊瑞莉雅','埃爾文','珍娜','嘉文四世','賈克斯','杰西','燼','吉茵珂絲','凱莎','克黎思妲','卡瑪','卡爾瑟斯','卡薩丁','卡特蓮娜','凱爾','慨影','凱能','卡力斯','鏡爪','克雷德','寇格魔','勒布朗','李星','雷歐娜','麗珊卓','路西恩','露璐','拉克絲','墨菲特','馬爾札哈','茂凱','易大師','好運姐','悟空','魔鬥凱薩','魔甘娜','娜米','納瑟斯','納帝魯斯','妮可','奈德麗','夜曲','努努和威朗普','歐拉夫','奧莉安娜','鄂爾','潘森','波比','派克','姬亞娜','葵恩','銳空','拉姆斯','雷珂煞','雷尼克頓','雷葛爾','雷玟','藍寶','雷茲','史瓦妮','薩科','慎','希瓦娜','辛吉德','賽恩','希維爾','史加納','索娜','索拉卡','斯溫','賽勒斯','星朵拉','貪啃奇','塔莉雅','塔隆','塔里克','提摩','瑟雷西','崔絲塔娜','特朗德','泰達米爾','逆命','圖奇','烏迪爾','烏爾加特','法洛士','汎','維迦','威寇茲','菲艾','維克特','弗拉迪米爾','弗力貝爾','沃維克','剎雅','齊勒斯','趙信','犽宿','約瑞科','悠咪','札克','劫','希格斯','極靈','柔依','枷蘿']
        await ctx.send(LOL_champion[random.randint(0,146)])

    @commands.command()
    async def 骰裝備(self,ctx):
        LOL_Item = ['深淵面具','大天使之杖','魔劍正宗','狂戰士護脛','輕靈之靴','法師之靴','冰霜之錘','寒冰霸拳','守護天使','時光之杖','海克斯科技 GLP-800','無盡之刃','致死宣告','多明尼克的問候','靈魂竊取者','終極魔劍','幻影之舞','忍者足具','錫柯的聚合之力','史特拉克手套','歐姆破壞者','振奮盔甲','日炎斗篷','昇華之骸','黑色切割者','嗜血者','狂怒九頭蛇','荊棘之甲','三相之力','好戰者鎧甲','芮蘭颶風箭','史提克彈簧刀','死亡之帽','智慧末刃','守望之骸','騎士誓願','冰霜之心','水星之靴','納什之牙','瑞萊的冰晶節杖','疾行之靴','鬼索的狂暴之刃','虛空之杖','水星彎刀','妖夢鬼刀','蘭頓之兆','海克斯科技槍刃','暮色黑刃','黎安卓的折磨','海克斯科技腰帶-01','殞落王者之劍','魔提斯深淵','中婭沙漏','愛歐尼亞之靴','精進之矛','黑魔禁書','雅典娜的惡魔聖杯','日輪的加冕','石像鬼磐核','適性神盔','米凱的魔鍋','盧登回音','星靈之骸','熾灼魔器','奪魄之鐮','虛空之門','死者肩甲','泰坦九頭蛇','榮耀頭盔','死亡之舞','夜色緣界','雙影斗篷','煉魔渾儀']
        await ctx.send(LOL_Item[random.randint(0,72)] + ' ' + LOL_Item[random.randint(0,72)] + ' ' + LOL_Item[random.randint(0,72)] + ' ' + LOL_Item[random.randint(0,72)] + ' ' + LOL_Item[random.randint(0,72)] + ' ' + LOL_Item[random.randint(0,72)])

    @commands.command()
    async def 骰技能(self,ctx):
        LOL_summonerspell = ['閃現  ','治癒  ','淨化  ','光盾  ','點燃  ','鬼步  ','傳送  ','虛弱  ']
        Str = ''
        for i in random.sample(LOL_summonerspell,2):
            Str += i
        await ctx.send(Str)

    @commands.command()
    async def 骰符文(self,ctx):
        LOL_runes=['precision','domination','sorcery','resolve','inspiration']
        chooseOne = {'precision':self.precision(),'domination':self.domination(),'sorcery':self.sorcery(),'resolve':self.resolve(),'inspiration':self.inspiration()}
        Str = chooseOne[random.choice(LOL_runes)]
        await ctx.send(Str)

    def precision(self):
        Str = "精準:\n"
        Str += self.precision_1()
        Str += self.precision_2()
        Str += self.precision_3()
        Str += self.precision_4() + "\n"
        Str += self.elseRunes(0)
        return Str

    def precision_1(self):
        Str = random.choice(['強攻  ','瞬疾步法  ','征服者  ','致命節奏  '])
        return Str

    def precision_2(self):
        Str = random.choice(['超量治癒  ','凱旋  ','氣定神閒  '])
        return Str

    def precision_3(self):
        Str = random.choice(['傳奇:敏捷  ','傳奇:韌性  ','傳奇:血脈  '])
        return Str

    def precision_4(self):
        Str = random.choice(['致命一擊  ','斬殺  ','背水一戰  '])
        return Str

    def domination(self):
        Str = "征服:\n"
        Str += self.domination_1()
        Str += self.domination_2()
        Str += self.domination_3()
        Str += self.domination_4() + "\n"
        Str += self.elseRunes(1)
        return Str

    def domination_1(self):
        Str = random.choice(['死亡電刑  ','掠食者  ','靈魂收割  ','刀鋒之雹  '])
        return Str

    def domination_2(self):
        Str = random.choice(['凌虐  ','血噬  ','即刻衝擊  '])
        return Str

    def domination_3(self):
        Str = random.choice(['殭屍守衛  ','幽靈普羅  ','眼球收集器  '])
        return Str

    def domination_4(self):
        Str = random.choice(['嗜血獵人  ','狡詐獵人  ','殘虐獵人  ','終焉獵人  '])
        return Str

    def sorcery(self):
        Str = "巫術:\n"
        Str += self.sorcery_1()
        Str += self.sorcery_2()
        Str += self.sorcery_3()
        Str += self.sorcery_4() + "\n"
        Str += self.elseRunes(2)
        return Str

    def sorcery_1(self):
        Str = random.choice(['召喚艾莉  ','奧術彗星  ','相位衝擊  '])
        return Str

    def sorcery_2(self):
        Str = random.choice(['除魔晶球  ','附魔之帶  ','光輝披風  '])
        return Str

    def sorcery_3(self):
        Str = random.choice(['卓越  ','迅捷  ','絕對專注  '])
        return Str

    def sorcery_4(self):
        Str = random.choice(['焦灼  ','水行者  ','暴風凝聚  '])
        return Str

    def resolve(self):
        Str = "意志:\n"
        Str += self.resolve_1()
        Str += self.resolve_2()
        Str += self.resolve_3()
        Str += self.resolve_4() + "\n"
        Str += self.elseRunes(3)
        return Str
    
    def resolve_1(self):
        Str = random.choice(['不死之握  ','裂地衝擊  ','神聖守護  '])
        return Str

    def resolve_2(self):
        Str = random.choice(['爆破  ','生命之泉  ','盾擊  '])
        return Str

    def resolve_3(self):
        Str = random.choice(['調節  ','回春  ','骨甲  '])
        return Str

    def resolve_4(self):
        Str = random.choice(['過度生長  ','甦醒  ','堅毅  '])
        return Str

    def inspiration(self):
        Str = "啟示:\n"
        Str += self.inspiration_1()
        Str += self.inspiration_2()
        Str += self.inspiration_3()
        Str += self.inspiration_4() + "\n"
        Str += self.elseRunes(4)
        return Str

    def inspiration_1(self):
        Str = random.choice(['冰川增幅  ','竊盜高手  ','啟封法書  '])
        return Str

    def inspiration_2(self):
        Str = random.choice(['海科斯充能閃現  ','魔法靈靴  ','完美計時  '])
        return Str

    def inspiration_3(self):
        Str = random.choice(['未來市集  ','小兵去質器  ','乾糧快遞  '])
        return Str

    def inspiration_4(self):
        Str = random.choice(['銀河視界  ','斗轉星移  ','時間扭曲藥水  '])
        return Str

    def elseRunes(self,num):
        Str = ""
        while Str == "" :
            temp = random.randint(0,4)
            if num != temp :
                chooseSec = {'0':random.sample([self.precision_2(),self.precision_3(),self.precision_4()],2),'1':random.sample([self.domination_2(),self.domination_3(),self.domination_4()],2),'2':random.sample([self.sorcery_2(),self.sorcery_3(),self.sorcery_4()],2),'3':random.sample([self.resolve_2(),self.resolve_3(),self.resolve_4()],2),'4':random.sample([self.inspiration_2(),self.inspiration_3(),self.inspiration_4()],2)}
                for i in chooseSec[str(temp)]:
                    Str += i
                Str += random.choice(['適性之力  ','攻擊速度  ','冷卻減免  '])
                Str += random.choice(['適性之力  ','物理防禦  ','魔法防禦  '])
                Str += random.choice(['生命  ','物理防禦  ','魔法防禦  '])
        return Str
def setup(bot):
    bot.add_cog(LOLBot(bot))