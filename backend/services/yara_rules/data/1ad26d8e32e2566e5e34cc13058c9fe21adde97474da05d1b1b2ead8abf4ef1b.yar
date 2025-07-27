rule auto_rule_20250727012330_0913 {
  strings:
    $o0 = "x402C20" wide ascii nocase
    $o1 = "dword_43B1B1" wide ascii nocase
    $o2 = "dword_43B104" wide ascii nocase
    $o3 = "dword_43B0B8" wide ascii nocase
    $o4 = "dword_43B20C" wide ascii nocase
  condition:
    4 of ($o*)
}