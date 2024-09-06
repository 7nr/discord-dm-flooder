import os, easygui, sys, discord, threading, ctypes, time, asyncio



def termSize():
    return int(int(os.get_terminal_size().columns) / 3)

################## IDK colors n shiii
logo = """
[38;2;144;66;245m.[38;2;142;70;245m▄[38;2;140;74;245m▄[38;2;138;78;245m [38;2;136;82;245m·[38;2;134;86;245m [38;2;132;90;245m [38;2;130;94;245m [38;2;128;98;245m [38;2;126;102;245m [38;2;124;106;245m [38;2;122;110;245m [38;2;120;114;245m▄[38;2;118;118;245m▄[38;2;116;122;245m▌[38;2;114;126;245m [38;2;112;130;245m [38;2;110;134;245m▄[38;2;108;138;245m•[38;2;106;142;245m [38;2;105;146;245m▄[38;2;103;150;245m▌[38;2;101;154;245m▄[38;2;99;158;245m▄[38;2;97;162;245m▄[38;2;95;166;245m▄[38;2;93;170;245m▄[38;2;91;174;245m▪[38;2;89;178;245m [38;2;87;182;245m [38;2;85;186;245m [38;2;83;190;245m [38;2;81;194;245m [38;2;79;198;245m [38;2;77;202;245m [38;2;75;206;245m [38;2;73;210;245m [38;2;71;214;245m▐[38;2;69;218;245m [38;2;67;222;245m▄[38;2;66;227;245m 
[38;2;144;66;245m▐[38;2;142;70;245m█[38;2;140;74;245m [38;2;138;78;245m▀[38;2;136;82;245m.[38;2;134;86;245m [38;2;132;90;245m▪[38;2;130;94;245m [38;2;128;98;245m [38;2;126;102;245m [38;2;124;106;245m [38;2;122;110;245m [38;2;120;114;245m█[38;2;118;118;245m█[38;2;116;122;245m•[38;2;114;126;245m [38;2;112;130;245m [38;2;110;134;245m█[38;2;108;138;245m▪[38;2;106;142;245m█[38;2;105;146;245m█[38;2;103;150;245m▌[38;2;101;154;245m•[38;2;99;158;245m█[38;2;97;162;245m█[38;2;95;166;245m [38;2;93;170;245m [38;2;91;174;245m█[38;2;89;178;245m█[38;2;87;182;245m [38;2;85;186;245m▪[38;2;83;190;245m [38;2;81;194;245m [38;2;79;198;245m [38;2;77;202;245m [38;2;75;206;245m [38;2;73;210;245m•[38;2;71;214;245m█[38;2;69;218;245m▌[38;2;67;222;245m▐[38;2;66;227;245m█
[38;2;144;66;245m▄[38;2;142;70;245m▀[38;2;140;74;245m▀[38;2;138;78;245m▀[38;2;136;82;245m█[38;2;134;86;245m▄[38;2;132;90;245m [38;2;130;94;245m▄[38;2;128;98;245m█[38;2;126;102;245m▀[38;2;124;106;245m▄[38;2;122;110;245m [38;2;120;114;245m█[38;2;118;118;245m█[38;2;116;122;245m▪[38;2;114;126;245m [38;2;112;130;245m [38;2;110;134;245m█[38;2;108;138;245m▌[38;2;106;142;245m▐[38;2;105;146;245m█[38;2;103;150;245m▌[38;2;101;154;245m [38;2;99;158;245m▐[38;2;97;162;245m█[38;2;95;166;245m.[38;2;93;170;245m▪[38;2;91;174;245m▐[38;2;89;178;245m█[38;2;87;182;245m·[38;2;85;186;245m [38;2;83;190;245m▄[38;2;81;194;245m█[38;2;79;198;245m▀[38;2;77;202;245m▄[38;2;75;206;245m [38;2;73;210;245m▐[38;2;71;214;245m█[38;2;69;218;245m▐[38;2;67;222;245m▐[38;2;66;227;245m▌
[38;2;144;66;245m▐[38;2;142;70;245m█[38;2;140;74;245m▄[38;2;138;78;245m▪[38;2;136;82;245m▐[38;2;134;86;245m█[38;2;132;90;245m▐[38;2;130;94;245m█[38;2;128;98;245m▌[38;2;126;102;245m.[38;2;124;106;245m▐[38;2;122;110;245m▌[38;2;120;114;245m▐[38;2;118;118;245m█[38;2;116;122;245m▌[38;2;114;126;245m▐[38;2;112;130;245m▌[38;2;110;134;245m▐[38;2;108;138;245m█[38;2;106;142;245m▄[38;2;105;146;245m█[38;2;103;150;245m▌[38;2;101;154;245m [38;2;99;158;245m▐[38;2;97;162;245m█[38;2;95;166;245m▌[38;2;93;170;245m·[38;2;91;174;245m▐[38;2;89;178;245m█[38;2;87;182;245m▌[38;2;85;186;245m▐[38;2;83;190;245m█[38;2;81;194;245m▌[38;2;79;198;245m.[38;2;77;202;245m▐[38;2;75;206;245m▌[38;2;73;210;245m█[38;2;71;214;245m█[38;2;69;218;245m▐[38;2;67;222;245m█[38;2;66;227;245m▌
[38;2;144;66;245m [38;2;142;70;245m▀[38;2;140;74;245m▀[38;2;138;78;245m▀[38;2;136;82;245m▀[38;2;134;86;245m [38;2;132;90;245m [38;2;130;94;245m▀[38;2;128;98;245m█[38;2;126;102;245m▄[38;2;124;106;245m▀[38;2;122;110;245m▪[38;2;120;114;245m.[38;2;118;118;245m▀[38;2;116;122;245m▀[38;2;114;126;245m▀[38;2;112;130;245m [38;2;110;134;245m [38;2;108;138;245m▀[38;2;106;142;245m▀[38;2;105;146;245m▀[38;2;103;150;245m [38;2;101;154;245m [38;2;99;158;245m▀[38;2;97;162;245m▀[38;2;95;166;245m▀[38;2;93;170;245m [38;2;91;174;245m▀[38;2;89;178;245m▀[38;2;87;182;245m▀[38;2;85;186;245m [38;2;83;190;245m▀[38;2;81;194;245m█[38;2;79;198;245m▄[38;2;77;202;245m▀[38;2;75;206;245m▪[38;2;73;210;245m▀[38;2;71;214;245m▀[38;2;69;218;245m [38;2;67;222;245m█[38;2;66;227;245m▪
"""
color1 = "[38;2;144;66;245m"
color2 = "[38;2;66;227;245m"
#################

def windowTitle():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Used Tokens: {onlineCount} | Messages Sent: {messagesSent} | MPM: {mpm} | Errors: {errors}")

def mpmCounter():
    global mpm
    while True:
        if messagesSent >= 1:
            now = messagesSent
            time.sleep(4) 
            mpm = (messagesSent - now) * 15

onlineCount = 0
messagesSent = 0
errors = 0
mpm = 0
async def DMflood(token: str, message: str, userID: int):
    '''Handles the user fetching & message sending'''
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        global onlineCount, messagesSent, errors
        onlineCount += 1
        reciever = await client.fetch_user(userID)
        while True:
            try:
                await reciever.send(message)
                messagesSent += 1
                sys.stdout.write(f"\r{color2}New Message Sent {color1}| {color2}Total Sent: {color1}{messagesSent}")
            except Exception as e:
                errors += 1
                print(e)
                await asyncio.sleep(2)

    await client.start(token)

def selectTokens():
    '''Beautiful file selection'''
    while True:
        sys.stdout.write(f"\r{color1}Select Your Token File:")
        tokenFilePath = easygui.fileopenbox(msg="Select file containing your bot tokens.", title="Select Token File", filetypes='*.txt', multiple=False)
        if tokenFilePath != None:
            print(f" {color2}{str(tokenFilePath.split('\\')[-1])}")
            break
    return tokenFilePath

async def start(tokens: list, message: str, userID: int):
    '''Smoothly transition between unasync & asnycio, starts the flooding with all tokens concurrently'''
    await asyncio.gather(*[DMflood(token, message, userID) for token in tokens])


def main():
    '''main function i assume?'''
    print(logo.replace("\n", "\n"+" "*termSize())) # prints the very cool logo in da middle of ya scween :3 
    tokens = selectTokens()
    tokens = open(tokens, "r", encoding="UTF8").read().splitlines()
    print(f"{color1}Successfully loaded: {color2}{len(tokens)} {color1}Token/s")
    userID = int(input(f"{color1}Enter Target userID: {color2}"))
    message = str(input(f"{color1}Enter Message To Send: {color2}"))
    print("\n")
    asyncio.run(start(tokens, message, userID))


if __name__ == "__main__":
    os.system("cls")
    threading.Thread(target=windowTitle).start()
    threading.Thread(target=mpmCounter).start()
    main()