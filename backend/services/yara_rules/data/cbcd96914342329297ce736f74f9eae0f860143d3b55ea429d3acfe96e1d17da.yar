rule auto_rule_20250727022126_8301 {
  strings:
    $o0 = "dword_42917B" wide ascii nocase
    $o1 = "xF89C85A1" wide ascii nocase
    $o2 = "off_428187" wide ascii nocase
    $o3 = "x35BF" wide ascii nocase
  condition:
    4 of ($o*)
}