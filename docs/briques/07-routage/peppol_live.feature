# language: fr
Fonctionnalité: Requêtes PEPPOL
    PEPPOL est un service DNS.
    Je dois pouvoir interroger ce service
    et obtenir les informations utiles au routage des factures.

    Contexte:
        Soit le service PEPPOL simulé avec:
            """
            sml: acc.edelivery.tech.ec.europa.eu
            entreprises:
            - id: e1
              smp: https://smp.pa-distante.fr
            - id: e2
              smp: https://smp.autre-pa.fr
            """


    Scénario: xxxxx

        #Soit l'entreprise #e1 avec le SIREN "123456789"
        #Et l'entreprise #e1 enregistrée sur PEPPOL
        #Quand j'interroge le SML via DNS
        #Alors j'obtiens une réponse DNS valide
        #Et j'obtiens l'URL du SMP "https://smp.pa-distante.fr"

