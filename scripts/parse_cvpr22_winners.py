import pyperclip


raw = """
Challenge: Natural Language Queries 

1st Place: ReLER@ZJU-Alibaba
Team: 

Naiyuan Liu (Zhejiang University, University of Technology Sydney)
Xiaohan Wang (Zhejiang University)
Xiaobo Li (Alibaba Group)
Yi Yang (Zhejiang University)
Yueting Zhuang (Zhejiang University)

Validation Report: https://arxiv.org/abs/2207.00383
Code: https://github.com/NNNNAI/Ego4d_NLQ_2022_1st_Place_Solution

2nd Place: EgoVLP
Team: 

Kevin Qinghong Lin (NUS)
Alex Jinpeng Wang (NUS)
Mattia Soldan (KAUST)
Michael Wray (University of Bristol)
Rui Yan (NUS)
Eric Zhongcong Xu (NUS)
Difei Gao (NUS)
Rongcheng Tu (Tencent)
Wenzhe Zhao (Tencent)
Weijie Kong (Tencent)
Chengfei Cai (Tencent)
Hongfa Wang (Tencent)
Dima Damen (University of Bristol)
Bernard Ghanem (KAUST)
Wei Liu (Tencent)
Mike Zheng Shou (NUS)

Validation Report: https://arxiv.org/abs/2207.01622
Code: https://github.com/showlab/EgoVLP

3rd Place: MSRA-AIM3_Teams
Team: 
Sipeng Zheng, Renmin University of China
Qi Zhang, Renmin University of China
Bei Liu, Microsoft Research
Qin Jin, Renmin University of China
Jianlong Fu, Microsoft Research

Validation Report: Forthcoming 
Code: Forthcoming 

Challenge: PNR Temporal Localization

1st Place: SViT
Team: 

Elad Ben-Avraham, Tel Aviv University
Roei Herzig, Tel Aviv University
Karttikeya Mangalam, UC Berkeley
Amir Bar, Tel Aviv University
Anna Rohrbach, UC Berkeley
Leonid Karlinsky, IBM-Research
Trevor Darrell, UC Berkeley
Amir Globerson, Tel Aviv University, Google



Validation Report: https://arxiv.org/pdf/2206.07689.pdf
Code: https://eladb3.github.io/SViT/

2nd Place: UniAndes
Team: 

Maria Escobar, Universidad de los Andes
Laura Daza, Universidad de los Andes
Cristina González, Universidad de los Andes
Jordi Pont-Tuset, Google
Pablo Arbelaez, Universidad de los Andes

Validation Report: https://arxiv.org/pdf/2207.11329.pdf 
Code: https://github.com/BCV-Uniandes/PNR_OSCC 

3rd Place: EgoVLP
Team: 

Kevin Qinghong Lin (NUS)
Alex Jinpeng Wang (NUS)
Mattia Soldan (KAUST)
Michael Wray (University of Bristol)
Rui Yan (NUS)
Eric Zhongcong Xu (NUS)
Difei Gao (NUS)
Rongcheng Tu (Tencent)
Wenzhe Zhao (Tencent)
Weijie Kong (Tencent)
Chengfei Cai (Tencent)
Hongfa Wang (Tencent)
Dima Damen (University of Bristol)
Bernard Ghanem (KAUST)
Wei Liu (Tencent)
Mike Zheng Shou (NUS)

Validation Report: https://arxiv.org/abs/2207.01622
Code: https://github.com/showlab/EgoVLP

Challenge: Object State Change Classification

1st Place: EgoVLP
Team: 
Kevin Qinghong Lin (NUS)
Alex Jinpeng Wang (NUS)
Mattia Soldan (KAUST)
Michael Wray (University of Bristol)
Rui Yan (NUS)
Eric Zhongcong Xu (NUS)
Difei Gao (NUS)
Rongcheng Tu (Tencent)
Wenzhe Zhao (Tencent)
Weijie Kong (Tencent)
Chengfei Cai (Tencent)
Hongfa Wang (Tencent)
Dima Damen (University of Bristol)
Bernard Ghanem (KAUST)
Wei Liu (Tencent)
Mike Zheng Shou (NUS)

Validation Report: https://arxiv.org/abs/2207.01622
Code: https://github.com/showlab/EgoVLP

2nd Place: TarHeels
Team: 
Md Mohaiminul Islam, UNC Chapel Hill
Gedas Bertasius, UNC Chapel Hill

Validation Report: https://arxiv.org/abs/2207.11814 
Code: https://github.com/md-mohaiminul/ObjectStateChange 

3rd Place: UniAndes
Team: 
Laura Daza, Universidad de los Andes
Maria Escobar, Universidad de los Andes
Cristina González, Universidad de los Andes
Jordi Pont-Tuset, Google
Pablo Arbelaez, Universidad de los Andes
Validation Report: https://arxiv.org/pdf/2207.11329.pdf 
Code: https://github.com/BCV-Uniandes/PNR_OSCC 

Challenge: Long Term Anticipation 

1st Place: Autonomous Systems
Team: 
Esteve Valls Mascaro, Technische Universtität Wien
Hyemin Ahn, Ulsan National Institute of Science and Technology (UNIST)
Dongheui Lee, Technische Universtität Wien
Validation Report: https://arxiv.org/abs/2207.12080
Code: https://github.com/Evm7/ego4dlta-icvae


2nd Place: RoboVision
Team: 
Srijan Das, Stony Brook University
Michael Ryoo, Stony Brook University, Google
Validation Report: https://arxiv.org/abs/2207.00579
Code: https://github.com/srijandas07/clip_baseline_LTA_Ego4d

Challenge: Visual Queries

1st Place: thereisnospoon
Team: 
Mengmeng Xu, KAUST
Juan-Manuel Perez-Rua, Facebook
Cheng-Yang Fu, Facebook
Yanghao Li, Facebook
Bernard Ghanem, KAUST
Tao Xiang, Facebook

Validation Report: Forthcoming 
Code: https://github.com/facebookresearch/vq2d_cvpr
"""

output_html = ""

evalai_links = {
    "Natural Language Queries": "https://eval.ai/web/challenges/challenge-page/1629/overview",
    "PNR Temporal Localization": "https://eval.ai/web/challenges/challenge-page/1622/overview",
    "Object State Change Classification": "https://eval.ai/web/challenges/challenge-page/1627/overview",
    "Long Term Anticipation": "https://eval.ai/web/challenges/challenge-page/1598/overview",
    "Visual Queries": "https://eval.ai/web/challenges/challenge-page/1619/overview",
}

newline = "\n"


def gen_html(context):
    x = f"""<tr>
        <td>{context['position']}</td>
        <td>
            <span class="winners-team-name">{context['team_name']}</span>
        <ul>
            {
                newline.join([
                    f'<li>{member}</li>' for member in context['team_members']
                ])
            }
        </ul>
        </td>
        <td>
        {
            f"<a href={context['validation_report']}>Validation Report</a>" if "Forthcoming" not in context['validation_report'] else "Forthcoming"
        }
        </td>
        <td>
        {
            f"<a href={context['code']}>Code</a>" if "Forthcoming" not in context['code'] else "Forthcoming"
        }
        </td>
    </tr>
    """

    return x


context = {}
last_context = ""

for line in raw.split("\n"):
    if line.startswith("Challenge"):
        if context.get("challenge") is not None:
            output_html += gen_html(context)
            output_html += "</table>"
        context["challenge"] = line.split(":")[1].strip()
        output_html += f"""
<a href={evalai_links[context['challenge']]}><h4 class="small-title align-center">{context['challenge']} <i class="fas fa-link"></i></h4></a>
<table class="winners-table">
    <tr>
        <th>Place</th>
        <th>Team</th>
        <th>Validation Report</th>
        <th>Code</th>
    </tr>"""
        last_context = "challenge"

    elif line.startswith("Team"):
        context["team_members"] = []
        last_context = "team_members"

    elif line.startswith("Validation Report"):
        context["validation_report"] = line[line.index(":") + 1 :]
        last_context = "validation_report"

    elif line.startswith("Code"):
        context["code"] = line[line.index(":") + 1 :]
        last_context = "code"

    elif line.startswith("1st Place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "1st Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif line.startswith("2nd Place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "2nd Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif line.startswith("3rd Place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "3rd Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif len(line) > 1:
        context["team_members"].append(line.strip())

output_html += gen_html(context)
output_html += "</table>"

print(output_html)
pyperclip.copy(output_html)