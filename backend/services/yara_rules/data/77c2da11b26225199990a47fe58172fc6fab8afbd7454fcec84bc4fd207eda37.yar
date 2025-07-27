rule auto_rule_20250726165438_5008 {
  strings:
    $o0 = "dword_43B67C" wide ascii nocase
    $o1 = "dword_43B0C2" wide ascii nocase
    $o2 = "x6EC3500u" wide ascii nocase
    $o3 = "off_43B1CA" wide ascii nocase
  condition:
    4 of ($o*)
}