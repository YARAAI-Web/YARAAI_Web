rule auto_rule_20250727044853_2742 {
  strings:
    $o0 = "chanparkcommit" wide ascii nocase
    $o1 = "putPtr" wide ascii nocase
    $o2 = "runtime__ptr_scavChunkData_alloc" wide ascii nocase
  condition:
    3 of ($o*)
}