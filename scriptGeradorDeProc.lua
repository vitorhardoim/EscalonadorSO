function criaArquivo(arqNome, n, minC, maxC, maxF)
	--<arrival time>, <priority>, <processor time>, <Mbytes>, <# impressoras>, <# scanners>, <# modems>, <# CDs>
	local arq = io.open(arqNome, "w")
	for i=1,n do
		arq:write(math.random(minC, maxC)..", "..math.random(0, 3)..", "..math.random(1, maxF)..", "..(2^math.random(0, 10))..", "..math.random(0, 2)..", "..math.random(0, 1)..", "..math.random(0, 1)..", "..math.random(0, 2).."\n")
	end
	arq:write(string.format("\n\n\nTotal processos: %d\tTempo mín. chegada: %d\tTempo máx. chegada: %d\tTempo máx duração: %d\t", n, minC, maxC, maxF))
	arq:flush()
	arq:close()
end

math.randomseed(os.time())
print("Nome do arquivo de processos: ")
local nome = io.read()
print("Total de processos: ")
local n = tonumber(io.read())
print("Tempo minimo de chegada dos processos: ")
local minCheg = tonumber(io.read())
print("Tempo maximo de chegada dos processos: ")
local maxCheg = tonumber(io.read())
print("Tempo maximo de duracao dos processos: ")
local maxFim = tonumber(io.read())
criaArquivo(nome, n, minCheg, maxCheg, maxFim)