rule auto_rule_20250726212151_6476 {
  strings:
    $o0 = "getsockname" wide ascii nocase
    $o1 = "dword_43B855" wide ascii nocase
    $o2 = "dword_43B57E" wide ascii nocase
    $o3 = "x2940A200u" wide ascii nocase
    $o4 = "dword_43B733" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726212152_9360 {
  strings:
    $o0 = "dword_43B1BE" wide ascii nocase
    $o1 = "dword_43B02C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726212156_4333 {
  condition:
    auto_rule_20250726212151_6476 or auto_rule_20250726212152_9360
}