rule auto_rule_20250727021349_6248 {
  strings:
    $o0 = "differ" wide ascii nocase
    $o1 = "SHDeleteValueA" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
    $o3 = "_heap_alloc" wide ascii nocase
  condition:
    4 of ($o*)
}