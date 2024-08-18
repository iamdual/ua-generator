from .ua_generator.data import browser_versions, browser_versions_idx_map

#Preprocessing
#Store the index of first appearance of a version in each browser_version list
for k,v in browser_versions.items():
    for idx,val in enumerate(v):
        if(val.major not in browser_versions_idx_map[k]):
            browser_versions_idx_map[k][val.major] = idx
       



