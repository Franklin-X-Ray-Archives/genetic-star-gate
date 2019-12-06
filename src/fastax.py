
import pyfastx
#ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR208/002/SRR2088062/SRR2088062_2.fastq.gz
for name, seq in pyfastx.Fasta('bgp.fasta', build_index=False):
    print(name, seq)
    
# get sequence counts in FASTA
fasta = pyfastx.Fasta('bgp.fasta')
print(len(fasta))


# get total sequence length of FASTA
print(fasta.size)

# get GC content of DNA sequence of FASTA
print(fasta.gc_content)

# get composition of nucleotides in FASTA
print(fasta.composition)
