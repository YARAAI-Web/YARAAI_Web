rule auto_rule_20250726165041_7688 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "dword_45C2D0" wide ascii nocase
  condition:
    all of them
}