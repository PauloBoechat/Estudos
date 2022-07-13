print('-='*20, 'ISTs', '=-'*20)

while True:
    print('''
1. Infecções bacterianas
2. Infecções virais
3. Infecções por fungos
4. Infecções por protosoarios
    ''')

#Infecções Bacterianas

    R = int(input('Qual tipo de infecção você quer conhecer primeiro? [1,2,3,4]: '))
    if R == 1:
        while True:
            print('-'*10, 'Bacterianas', '-'*10)
            print('''
1. Gonorreia
2. Sífilis
3. Clamídia
            ''')

            R2 = int(input('Selecione a infecção que deseja conhecer [1,2,3]: '))
            if R2 == 1:
                print('='*10, 'Gonorreia', '='*10)
                print('''
\033[1mAgente causador: \033[0mBactéria Neisseria gonorrhoeae.

\033[1mTransmissão: \033[0mRelações sexuais desprotegidas ou da mãe para o bebê, no momento do parto.

\033[1mSintomas: \033[0mNo homem, os sintomas mais comuns são dor e ardência na região genital e eliminação de uma secreção branca ou amarelada ao urinar. Na mulher, em geral, não há sintomas; no entanto, a secreção vaginal pode ficar amarelada.

\033[1mPrevenção: \033[0mUso de preservativo nas relações sexuais.

\033[1mTratamento: \033[0mO tratamento é feito com o uso de antibióticos.
                ''')
            elif R2 == 2:
                print('='*10, 'Sífilis', '='*10)
                print('''
\033[1mAgente causador: \033[0mBactéria Treponema pallidum.

\033[1mTransmissão: \033[0mContato com feridas na pele e nas mucosas, transfusão de sangue ou da mãe para o bebê, durante a gestação, o parto ou a amamentação.

\033[1mSintomas: \033[0mO primeiro sintoma é uma ferida sem dor, com bordas duras, elevadas e
avermelhadas na área que entrou em contato com a bactéria (órgãos genitais, ânus,
boca, pele). Algumas semanas depois, a ferida some, mas a bactéria continua no or-
ganismo. Caso não seja tratada, alguns meses depois, surgem feridas na pele, febre
e dores nas articulações e nos músculos. Esses sinais também desaparecem após
algumas semanas, mesmo sem tratamento. Caso não seja tratada, pode ser fatal ao
atingir o coração, as artérias e o sistema nervoso. O diagnóstico é feito por exame
de sangue. Mulheres grávidas devem realizar o teste, porque a sífilis congênita pode
causar problemas físicos e mentais no bebê e até aborto.

\033[1mPrevenção: \033[0mUso de preservativo nas relações sexuais e acompanhamento pré-
-natal em gestantes.

\033[1mTratamento: \033[0mO tratamento é feito com o uso de antibióticos.
                ''')
            else:
                print('-'*10, 'Clamídia', '-'*10)
                print('''
\033[1mAgente causador: \033[0mBactéria Chlamydia trachomatis.

\033[1mTransmissão: \033[0mRelações sexuais desprotegidas ou da mãe para o bebê, no momento do parto.

\033[1mSintomas: \033[0mPode causar infecções na uretra, provocando dor e ardência ao urinar, nos olhos e
nos linfonodos da região genital, provocando inchaço na virilha. Na mulher, pode atingir tam-
bém o útero e as tubas uterinas, causando sangramento entre as menstruações, dor durante o
ato sexual, entre outros sintomas. Se não for tratada adequadamente, há risco de esterilidade.

\033[1mPrevenção: \033[0mUso de preservativo nas relações sexuais.

\033[1mTratamento: \033[0mO tratamento é feito com o uso de antibióticos.
                ''')
            
            E = input('Deseja conhecer mais infecções bacterianas? [S/N]: ').upper().strip()
            if E in 'SN':
                if E == 'N':
                    print('-'*50)
                    break
                else:
                    continue

#Infecções Virais

    if R == 2:
        while True:
            print('-'*10, 'Virais', '-'*10)
            print('''
1. HPV(Condiloma acuminado)
2. HIV(Aids)
3. Herpes-Vírus
4. Hepatite B
            ''')
            R2 = int(input('Selecione a infecção que deseja conhecer [1,2,3]: '))
            if R2 == 1:
                print('-'*10, 'HPV(Condiloma acuminado)', '-'*10)
                print('''
\033[1mAgente causador: \033[0mPapilomavírus humano (HPV, do inglês human papillomavirus).

\033[1mTransmissão: \033[0mRelações sexuais desprotegidas e da mãe para o bebê, no momento do parto.

\033[1mSintomas: \033[0mFormação de verrugas ou feridas nos órgãos genitais, no colo do útero ou ao redor
do ânus. A infecção persistente do HPV está associada ao câncer de colo de útero, de vulva, de
ânus, entre outros. Uma parte dos casos pode ser assintomática.

\033[1mPrevenção: \033[0mVacinação contra os tipos de HPV mais comuns, que têm como público-alvo meninas
de 9 a 14 anos e meninos de 11 a 14 anos (Figura 3), e uso de preservativo nas relações sexuais.

\033[1mTratamento: \033[0mEliminação das lesões por meio de congelamento, bisturi elétrico, laser, cirurgia ou
produtos químicos. O exame ginecológico conhecido como papanicolau pode detectar alterações
no colo do útero e indicar uma possível infecção por HPV.
                ''')
            elif R2 == 2:
                print('-'*10, 'HIV(Aids)', '-'*10)
                print('''
\033[1mAgente causador: \033[0mVírus da imunodeficiência adquirida (HIV, do inglês human immunodeficiency virus).

\033[1mTransmissão: \033[0mRelações sexuais desprotegidas; transfusão de sangue; contato com secreções; da
mãe para o bebê, no momento do parto e na amamentação.

\033[1mSintomas: \033[0mO vírus infecta células do sistema imune (linfócitos) e utiliza suas estruturas para se
multiplicar. Os novos vírus, ao serem liberados, destroem a membrana da célula hospedeira, que
deixa de atuar na proteção do organismo, tornando-o vulnerável a outras doenças.

\033[1mPrevenção: \033[0mUsar preservativo nas relações sexuais, evitar o compartilhamento de materiais
perfurantes ou cortantes, acompanhamento médico de gestantes e utilização de agulhas e
seringas descartáveis.

\033[1mTratamento: \033[0mEmbora o vírus não possa ser eliminado do organismo, existem medicamentos
que impedem o avanço da doença.
                ''')
            elif R2 == 3:
                print('-'*10, 'Herpes-Vírus', '-'*10)
                print('''
\033[1mAgente causador: \033[0mAs IST causadas por vírus da família Herpesviridae são de dois tipos principais: um
deles ataca geralmente os lábios e a face (herpes labial), e o outro, a região genital (herpes genital).

\033[1mTransmissão: \033[0mContato direto com as feridas ou indireto com objetos contaminados.

\033[1mSintomas: \033[0mO primeiro sintoma é vermelhidão e coceira local. Em seguida, surgem pequenas bolhas
que estouram e formam feridas. Os sintomas desaparecem geralmente em até quatro semanas, mas
o vírus continua no organismo. Em algumas pessoas, há recaídas, isto é, reaparições das lesões na
área afetada. Não se deve furar as bolhas, aplicar pomadas no local sem recomendação médica nem
ter relações sexuais desprotegidas durante as recaídas (período em que o risco de contágio é maior).

\033[1mPrevenção: \033[0mEvitar o contato com as feridas ou objetos de uso pessoal e usar preservativo nas
relações sexuais.

\033[1mTratamento: \033[0mEmbora o vírus não possa ser eliminado do organismo, existem medicamentos que
diminuem os sintomas e os riscos de transmissão da doença.
                ''')
            else:
                print('-'*10, 'Hepatite B', '-'*10)
                print('''
\033[1mAgente causador: \033[0mA hepatite pode ser causada por diferentes tipos de vírus. Os tipos mais co-
muns são os da hepatite A, B e C, mas apenas o tipo B é considerado IST.

\033[1mTransmissão: \033[0mTransfusão de sangue; relação sexual desprotegida; contato com mucosas e secre-
ções, como a saliva e as lágrimas; da mãe para o feto através da placenta ou no momento do parto.

\033[1mSintomas: \033[0mInflamação do fígado, que provoca febre, dor de cabeça, cansaço e, geralmente,
icterícia. Em alguns casos, pode provocar cirrose (doença crônica do fígado) ou câncer de fígado.

\033[1mPrevenção: \033[0mVacinação e uso de preservativo nas relações sexuais.

\033[1mTratamento: \033[0mNa maioria dos casos, o tratamento tem como objetivo aliviar os sintomas e
reduzir o risco de complicações.
                ''')

            E = input('Deseja conhecer mais infecções Virais? [S/N]: ').upper().strip()
            if E in 'SN':
                if E == 'N':
                    print('-'*50)
                    break
                else:
                    continue

#Fugos

    if R == 3:
        while True:
            print('-'*10, 'fungos', '-'*10)
            print('''
1. Candidíase
            ''')
            R2 = int(input('Selecione a infecção que deseja conhecer [1]: '))
            print('-'*10, 'Candidíase', '-'*10)
            print('''
\033[1mAgente causador: \033[0mFungo Candida albicans.

\033[0mTransmissão: \033[0mRelações sexuais desprotegidas.

\033[1mSintomas: \033[0mNa mulher, uma secreção esbranquiçada, acompanhada de coceira, aparece nos órgãos
genitais. No homem, pode provocar vermelhidão e coceira na área genital. Em alguns casos, o
fungo pode estar presente no organismo sem provocar sintomas, mas, quando o sistema imune
está enfraquecido, ele pode se multiplicar e causar a doença.

\033[1mPrevenção: \033[0mUso de preservativo nas relações sexuais; é necessário manter a região genital seca e evitar
o consumo excessivo de antibióticos, que favorecem a proliferação de formas resistentes do fungo.

\033[1mTratamento: \033[0mUso de pomadas, cremes ou outros medicamentos indicados pelo médico.
            ''')
            E = input('Deseja conhecer mais infecções Virais? [S/N]: ').upper().strip()
            if E in 'SN':
                if E == 'N':
                    print('-'*50)
                    break
                else:
                    continue

#Protozoários

    if R == 4: 
        while True:
            print('-'*10, 'Protozoários', '-'*10)
            print('''
1. Tricomoníase
2. Pediculose pubiana
            ''')
        
            R2 = int(input('Selecione a infecção que deseja conhecer [1,2]: '))
            if R2 == 1:
                print('-'*10, 'Tricomoníase', '-'*10)
                print('''
\033[1mAgente causador: \033[0mProtozoário Trichomonas vaginalis (Figura 5).

\033[1mTransmissão: \033[0mRelações sexuais desprotegidas ou contato com secreções.

\033[1mSintomas: \033[0mPode ser assintomática ou provocar ardência e dificuldade para urinar, dor durante a relação sexual e coceira nos órgãos sexuais.

\033[1mPrevenção: \033[0mUso de preservativo nas relações sexuais.

\033[1mTratamento: \033[0mUso de medicamentos que causam a morte do protozoário.
                ''')
            if R2 == 2:
                print('-'*10, 'Pediculose', '-'*10)
                print('''
\033[1mAgente causador: \033[0mPiolho-púbico (Pthirus pubis), inseto conhecido popularmente como chato.

\033[1mTransmissão: \033[0mPode ocorrer tanto por contato sexual como por compartilhamento de roupas, toalhas ou lençóis.

\033[1mSintomas: \033[0mO principal sintoma é a coceira. Nos locais da picada, podem ocorrer alterações na pele semelhantes à urticária, bolhas e manchas azuladas.

\033[1mPrevenção: \033[0mManter a região pubiana higienizada, evitando o contato com piolhos e impedindo a fixação de lêndeas (ovos).

\033[1mTratamento: \033[0mUso de medicamentos específicos para eliminar os insetos e os ovos das regiões afetadas.
                ''')
            E = input('Deseja conhecer mais infecções por protozoarios? [S/N]: ').upper().strip()
            if E in 'SN':
                if E == 'N':
                    print('-'*50)
                    break
                else:
                    continue
    E = input('Deseja conhecer mais ISTs? [S/N]: ').upper().strip()
    if E in 'SN':
        if E == 'N':
            print('Obrigado por usar o app')
            break
        else:
            continue