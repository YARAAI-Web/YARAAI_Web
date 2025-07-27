rule auto_rule_20250726101233_5727 {
  strings:
    $o0 = "ppSacl" wide ascii nocase
    $o1 = "BackupEventLogA" wide ascii nocase
    $o2 = "bAutoScroll" wide ascii nocase
    $o3 = "ImageList_Create" wide ascii nocase
    $o4 = "ObjectTypeListLength" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726101236_0436 {
  strings:
    $o0 = "SHFreeNameMappings" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726101241_9292 {
  condition:
    auto_rule_20250726101233_5727 or auto_rule_20250726101236_0436
}