rule auto_rule_20250726080225_3404 {
  strings:
    $o0 = "off_4283F5" wide ascii nocase
    $o1 = "xF89C95B9" wide ascii nocase
    $o2 = "x2D0Au" wide ascii nocase
    $o3 = "dword_428E25" wide ascii nocase
  condition:
    4 of ($o*)
}