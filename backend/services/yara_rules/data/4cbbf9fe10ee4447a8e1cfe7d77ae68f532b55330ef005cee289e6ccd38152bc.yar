rule auto_rule_20250726085128_0546 {
  strings:
    $o0 = "found_bx" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "__isctype_mt" wide ascii nocase
  condition:
    3 of ($o*)
}