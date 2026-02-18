cid = str(input('Em que cidade você nasceu? R.: ')).strip()
# NOTA & Comentário: ".strip()" elimina o ESPAÇO! Portanto, o ponha no início.

# Comentário PROF.: Atente-se à programação aceitar Minúsculo e Maiúsculo;
# [CONTINUAÇÃO] Como também, pode ter ESPAÇO no início. Isso vai dar erro!

# print(cid[:5] == 'Santo')
# Comentário PROF.: Resolva o problema até então, jogando tudo ou p/ Minúsculo ou p/ Maiúsculo;

print(cid[:5].upper() == 'SANTO')
# Comentário PROF.¹: Logo, por exemplo, use o ".upper()" + 'nome_Maiúsculo'. Veja em cima!
# [CONTINUAÇÃO] PROF.²: Assim,em ".upper() == 'SANTO')" tudo do 'input()' vai p/ Maiúsculo!
# [CONTINUAÇÃO] PROF.³: "Você como programador, sempre tem que pensar se o usuário via fazer besteira"; O fluxo!
