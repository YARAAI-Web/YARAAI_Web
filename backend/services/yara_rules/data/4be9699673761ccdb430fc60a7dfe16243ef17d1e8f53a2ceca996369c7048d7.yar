rule auto_rule_20250727025143_2118 {
  strings:
    $o0 = "GdipAlloc" wide ascii nocase
    $o1 = "off_475204" wide ascii nocase
    $o2 = "dword_4756AC" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
    $o4 = "off_418120" wide ascii nocase
  condition:
    4 of ($o*)
}