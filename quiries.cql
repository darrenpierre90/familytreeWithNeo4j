MATCH grandparents= (grandparent:Person) - [:Is_Parent_OF*2] ->(grandkid:Person)
return grandkid,grandparent

MATCH siblings= (parent:Person) - [:Is_Parent_OF] ->(target:Person)
Match (parent) - [:Is_Parent_OF] -> (sibling:Person)
return sibling