rule auto_rule_20250726113557_6464 {
  strings:
    $o0 = "x1FABCE00" wide ascii nocase
    $o1 = "dword_43B085" wide ascii nocase
    $o2 = "dword_43B4C4" wide ascii nocase
    $o3 = "byte_43B6BB" wide ascii nocase
    $o4 = "x6EC3500u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726113559_5654 {
  strings:
    $o0 = "dword_43B506" wide ascii nocase
    $o1 = "x53C70C00u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726113603_8669 {
  condition:
    auto_rule_20250726113557_6464 or auto_rule_20250726113559_5654
}