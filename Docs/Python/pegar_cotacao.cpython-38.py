U
    �Vvd"  �                   @   s2   d dl Z dd� Zedkr.eedd�� ed� dS )�    Nc              	   C   s�   t dd��}|�� �d�}W 5 Q R X | |kr4td� ||krDtd� d| � d|� �}t�|�}|rz|�� | |  d }|S td	� d
S d S )Nzcodigos_moedas.txt�r�
u   Moeda de Origem não encontradau    Moeda de Destino não encontradaz(https://economia.awesomeapi.com.br/last/�-Zbidu"   Combinação não existente na API� )�open�read�split�print�requests�getZjson)Zmoeda_origemZmoeda_destino�arquivoZcodigos_moedas�linkZ
requisicao�cotacao� r   �:c:\Users\leonardo\Documents\GitHub\python\pegar_cotacao.py�pegar_cotacao_atual   s    
r   �__main__ZEUR�BRLu   lira é doidao)r
   r   �__name__r	   r   r   r   r   �<module>   s   