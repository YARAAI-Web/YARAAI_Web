rule auto_rule_20250726093934_1275 {
  strings:
    $o0 = "dword_43B20C" wide ascii nocase
    $o1 = "dword_43B2CC" wide ascii nocase
    $o2 = "x40B71D00" wide ascii nocase
    $o3 = "dword_43B368" wide ascii nocase
    $o4 = "dword_43B05C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726093937_5129 {
  strings:
    $o0 = "dword_43B6FB" wide ascii nocase
    $o1 = "dword_43B3E3" wide ascii nocase
    $o2 = "getprotobyname" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726093940_5313 {
  condition:
    auto_rule_20250726093934_1275 or auto_rule_20250726093937_5129
}