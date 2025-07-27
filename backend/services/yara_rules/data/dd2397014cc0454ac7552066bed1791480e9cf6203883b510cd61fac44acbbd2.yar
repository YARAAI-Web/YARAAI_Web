rule auto_rule_20250726133549_5228 {
  strings:
    $o0 = "off_472078" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_4728C0" wide ascii nocase
    $o3 = "hard" wide ascii nocase
  condition:
    4 of ($o*)
}