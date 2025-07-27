rule auto_rule_20250726141053_7291 {
  strings:
    $o0 = "off_44DD30" wide ascii nocase
    $o1 = "_heap_alloc" wide ascii nocase
  condition:
    all of them
}