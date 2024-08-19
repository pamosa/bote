import discord
import os
import random  # Certifique-se de importar o módulo random
from discord.ext import commands
from keep_alive import keep_alive

# Mantenha o servidor web ativo
keep_alive()

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Lista de imagens de cavalo
cavalo_images = [
    'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia16043/caracteristicas-cavalos-saudaveis-artigos-cursos-cpt.jpg',
    'https://s1.static.brasilescola.uol.com.br/be/conteudo/images/cavalo.jpg',
    'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia25135/cavalo-pelagem-cpt.jpg',
    'https://super.abril.com.br/wp-content/uploads/2022/07/SI_441_ORCL_potencia_site.jpg?quality=90&strip=info&w=720&h=440&crop=1',
    'https://blog.7mboots.com.br/wp-content/uploads/2020/06/the-black-horse-of-the-frisian-breed-walks-in-the-P77UURU_Easy-Resize.com_.jpg',
    'https://static.wikia.nocookie.net/mundo-animal/images/a/a1/Cavalos-selvagens-cavlos.jpg/revision/latest?cb=20140328222555&path-prefix=pt',
    'https://vedovatipisos.com.br/wp-content/uploads/2016/10/4.jpg',
    'https://www.petz.com.br/blog/wp-content/uploads/2022/06/por-que-cavalo-usa-ferradura-2.jpg',
    'https://files.agro20.com.br/uploads/2019/09/cavalo-3-1024x576.jpg',
    'https://framerusercontent.com/images/hJdquuZWHdjptkuBFuSnd4snRLs.jpg',
    'https://fazendadaroseta.com.br/wp-content/uploads/2021/02/cavalos-mais-bonitos-do-mundo.jpg',
    'https://framerusercontent.com/images/of2Zi78PVMok6TmLryQLI7djbt0.jpeg',
    'https://www.infoescola.com/wp-content/uploads/2008/05/cavalo-143531608.jpg',
    'https://premix.com.br/blog/wp-content/uploads/2021/03/racas_cavalo_thumbnail.png',
    'https://www.cavaloatleta.com.br/wp-content/uploads/2023/01/cavalodeesporte.jpg',
    'https://blog.cobasi.com.br/wp-content/uploads/2023/05/quantos-anos-vive-cavalo-capa.webp',
    'https://www.comprerural.com/wp-content/uploads/2023/07/cavalo-1-750x430.jpg',
    'https://blog.buscarrural.com/wp-content/uploads/2021/02/cavalo-campolina-1.jpg',
    'https://www.jornalopcao.com.br/wp-content/uploads/2024/02/Gypsy-Vanner-e-grande-na-altura-e-na-docilidade-01-Karakal-1-1.jpg.webp',
    'https://kinghorse.com.br/wp-content/uploads/2018/03/racas-de-cavalo.jpg',
    'https://i0.wp.com/zootecniabrasil.com/wp-content/uploads/2023/06/lipizzan-cavalo-diferente.jpg?fit=851%2C567&ssl=1',
    'https://quero-ser-veterinario.s3.amazonaws.com/wp-content/uploads/queroserveterinario/destaque-cavalo-puro-sangue.webp',
    'https://www.lancerural.com.br/wp-content/uploads/2020/03/febrecavalo-scaled.jpg'
]

# Lista de frases de cavalo
cavalo_frases = [
    "Minerva sempre foi conhecido pela sua astúcia e força, mas ao lado dos cavalos, ele encontrou uma conexão única, onde força e velocidade se uniam em perfeita harmonia.",
    "Os cavalos corriam livres pelos campos, e Minerva os observava com admiração. Ele sabia que não poderia dominá-los, mas respeitava sua liberdade e espírito indomável.",
    "Minerva não temia a batalha, mas ao ver os cavalos correndo, ele percebeu que às vezes a verdadeira força está em saber quando seguir em frente e quando parar.",
    "Os cavalos eram rápidos, e Minerva, sábio. Ele entendeu que não precisava vencê-los, mas sim aprender com eles, adaptando sua força à velocidade do tempo.",
    "Minerva, em sua grandeza, não viu nos cavalos adversários, mas companheiros de jornada. Juntos, seguiram caminhos que ninguém havia trilhado antes.",
    "Na corrida da vida, Minerva e os cavalos seguiam em ritmos diferentes. Ele, com sua sabedoria, compreendia que não se tratava de vencer, mas de viver cada momento.",
    "Os cavalos o ultrapassaram, mas Minerva não se importou. Ele sabia que sua força não estava na velocidade, mas na resistência ao longo do tempo.",
    "Minerva viu os cavalos passarem e entendeu que não se trata sempre de ser o primeiro, mas de apreciar o caminho, mesmo quando outros estão à frente.",
    "Ele era bom mesmo?\nQuem? O Minerva? Ah, ele foi ótimo, um lutador perfeito, ninguém foi melhor que ele\nE como os cavalos venceram ele?\nO tempo venceu ele... o tempo vence todo mundo, é invencível..."
] * 3  # Replicando as frases para que o número corresponda ao número de imagens

# Lista de imagens e frases de centauro
centauro_images = [
    'https://deusesgregos.com.br/wp-content/uploads/2023/06/centauromitologia1.jpg',
    'https://deusesgregos.com.br/wp-content/uploads/2023/06/centauromitologia1.jpg',
    'https://segredosdomundo.r7.com/wp-content/uploads/2020/05/centauro-origem-do-migo-representacoes-e-principal-figura-1.jpg',
    'https://pm1.aminoapps.com/7041/334f3d6571fa0d3a5bd4f9241e246b87c1bc6367r1-424-512v2_00.jpg',
    'https://super.abril.com.br/wp-content/uploads/2018/07/5672e0730e2163522f019a04harry-potter.jpeg',
    'https://www.mitografias.com.br/wp-content/uploads/2015/06/Centauro-01.jpg',
    'https://pm1.aminoapps.com/6535/a7c6c31f0c5a02c261a3200d965942787800a27b_00.jpg',
    'https://i.pinimg.com/550x/5d/bb/b8/5dbbb8afe56fe5c315ef6d1d16ce069e.jpg',
    'https://mitologiaclasica.com/wp-content/uploads/2024/02/centauro.jpg',
    'https://c.wallhere.com/photos/29/24/fantasy_art_Centaur-193205.jpg!d',
    'https://mediafiles.fartice.com/imfls/97a5afea3d6a207c.jpg',
    'https://www.greenme.com.br/wp-content/uploads/2020/11/centauro-2.jpg',
    'https://i.pinimg.com/236x/cb/0a/e0/cb0ae0072f84bdbabd1fb6b58d675ee4.jpg',
    'https://i.pinimg.com/236x/50/dd/49/50dd49f3c84c0ae08c5473f82f59bbe8.jpg',
    'https://i.pinimg.com/236x/cb/0a/e0/cb0ae0072f84bdbabd1fb6b58d675ee4.jpg'
]

centauro_frases = [
    frase.replace('cavalo', 'centauro').replace('cavalos', 'centauros')
    for frase in cavalo_frases
]


@bot.event
async def on_ready():
    print(f'Bot {bot.user} está pronto e conectado!')
    await bot.change_presence(activity=discord.Game(
        name="https://minervinhacavalos.shop/"))
    try:
        synced = await bot.tree.sync(
            guild=None)  # Sincronizar comandos de barra globalmente
        print(f'Sincronizados {len(synced)} comandos de barra.')
    except Exception as e:
        print(f'Erro ao sincronizar os comandos: {e}')


# Comando normal para !cavalo
@bot.command(name='cavalo')
async def cavalo(ctx):
    random_index = random.randint(0, len(cavalo_images) - 1)
    image_url = cavalo_images[random_index]
    frase = cavalo_frases[random_index]
    embed = discord.Embed(description=frase)
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


# Comando normal para !centauro
@bot.command(name='centauro')
async def centauro(ctx):
    random_index = random.randint(0, len(centauro_images) - 1)
    image_url = centauro_images[random_index]
    frase = centauro_frases[random_index]
    embed = discord.Embed(description=frase)
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


# Slash command para /cavalo
@bot.tree.command(name='cavalo',
                  description='Receba uma imagem e frase de cavalo')
async def slash_cavalo(interaction: discord.Interaction):
    random_index = random.randint(0, len(cavalo_images) - 1)
    image_url = cavalo_images[random_index]
    frase = cavalo_frases[random_index]
    embed = discord.Embed(description=frase)
    embed.set_image(url=image_url)
    await interaction.response.send_message(embed=embed)


# Slash command para /centauro
@bot.tree.command(name='centauro',
                  description='Receba uma imagem e frase de centauro')
async def slash_centauro(interaction: discord.Interaction):
    random_index = random.randint(0, len(centauro_images) - 1)
    image_url = centauro_images[random_index]
    frase = centauro_frases[random_index]
    embed = discord.Embed(description=frase)
    embed.set_image(url=image_url)
    await interaction.response.send_message(embed=embed)


from keep_alive import keep_alive

# Código do bot, incluindo bot.run()
bot.run(os.getenv('DISCORD_TOKEN'))
