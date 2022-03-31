# NESSE PROGRAMA IREMOS CALCULAR A ÁREA TOTAL DE UM CUBO

aresta = float(input("\nDigite a medida (em centímetro) de uma das arestas(lados) do cubo: "))
area_da_base_do_cubo = aresta*aresta
area_lateral_do_cubo = (area_da_base_do_cubo)*4
area_total_do_cubo = (area_da_base_do_cubo)*6

print(f"\nA Área da Base do Cubo tem: {area_da_base_do_cubo}cm²")
print(f"A Área Lateral do Cubo tem: {area_lateral_do_cubo}cm²")
print(f"A Área Total do Cubo tem: {area_total_do_cubo}cm²\n")