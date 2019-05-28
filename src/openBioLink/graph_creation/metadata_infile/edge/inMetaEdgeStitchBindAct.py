from edgeType import EdgeType
from graph_creation.types.infileType import InfileType
from graph_creation.metadata_infile.infileMetadata import InfileMetadata
from nodeType import NodeType


class InMetaEdgeStitchBindAct(InfileMetadata):
    CSV_NAME = "DB_STITCH_drug_bindAct_gene.csv"
    USE_COLS = ['item_id_a', 'item_id_b', 'score']
    NODE1_COL = 0
    NODE2_COL = 1
    QSCORE_COL = 2
    NODE1_TYPE = NodeType.DRUG
    NODE2_TYPE = NodeType.GENE
    EDGE_TYPE = EdgeType.DRUG_BINDACT_GENE
    INFILE_TYPE = InfileType.IN_EDGE_STITCH_BINDACT


    MAPPING_SEP = None

    def __init__(self):
        super().__init__(csv_name=InMetaEdgeStitchBindAct.CSV_NAME,
                         cols=self.USE_COLS,
                         infileType=InMetaEdgeStitchBindAct.INFILE_TYPE)