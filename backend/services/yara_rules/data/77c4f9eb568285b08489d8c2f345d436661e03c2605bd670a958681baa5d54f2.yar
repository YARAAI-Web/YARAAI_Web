rule auto_rule_20250726185912_7537 {
  strings:
    $o0 = "x417230" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "dword_41A018" wide ascii nocase
    $o3 = "x3FFFu" wide ascii nocase
  condition:
    4 of ($o*)
}