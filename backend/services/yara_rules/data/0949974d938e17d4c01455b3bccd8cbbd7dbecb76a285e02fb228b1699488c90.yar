rule auto_rule_20250726095323_7147 {
  strings:
    $o0 = "fdwDetails" wide ascii nocase
    $o1 = "FlushFileBuffers" wide ascii nocase
    $o2 = "strcat" wide ascii nocase
    $o3 = "_calloc_dbg" wide ascii nocase
  condition:
    4 of ($o*)
}