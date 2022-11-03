import basf2 as b2
import modularAnalysis as ma
import vertex as vx

gbasf2_dataset = []  # gbasf2 will figure this out
from extravariables import runningOnMC, outputfile

mypath = b2.create_path()
ma.inputMdstList(
    environmentType="default",
    filelist=gbasf2_dataset,
    path=mypath,
    entrySequences=["0:10"],
)

ma.fillParticleList(
    decayString="K+:1%",
    cut="dr < 0.5 and abs(dz) < 3 and thetaInCDCAcceptance and kaonID > 0.01",
    path=mypath,
)
ma.fillParticleList(
    decayString="pi+:my",
    cut="dr < 0.5 and abs(dz) < 3 and thetaInCDCAcceptance",
    path=mypath,
)

ma.reconstructDecay(
    decayString="D-:K2Pi -> K+:1% pi-:my pi-:my", cut="1.5 < M < 2.2", path=mypath
)

ma.reconstructDecay(
    decayString="B0:PiD-toK2Pi -> D-:K2Pi pi+:my",
    cut="5.0 < Mbc and abs(deltaE) < 1.0",
    path=mypath,
)
vx.treeFit(
    "B0:PiD-toK2Pi",
    -1,
    path=mypath,
    updateAllDaughters=False,
    ipConstraint=True,
    massConstraint=[-411, 411],
)
ma.applyCuts("B0:PiD-toK2Pi", "5.2 < Mbc and abs(deltaE) < 0.5", path=mypath)

# dump in MDST format
import mdst as mdst

mdst.add_mdst_output(
    path=mypath,  # use mdst for further modification using basf2, nTuples for offline
    mc=runningOnMC,
    filename=outputfile,
)

b2.process(mypath)
print(b2.statistics)
