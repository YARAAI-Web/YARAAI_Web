rule auto_rule_20250726194825_3120 {
  strings:
    $o0 = "dword_464D70" wide ascii nocase
    $o1 = "__sbh_alloc_block" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
    $o3 = "x1004u" wide ascii nocase
  condition:
    4 of ($o*)
}