rule auto_rule_20250726163731_2149 {
  strings:
    $o0 = "dword_43B5FA" wide ascii nocase
    $o1 = "dword_43B3F2" wide ascii nocase
    $o2 = "dword_43B451" wide ascii nocase
    $o3 = "dword_43B239" wide ascii nocase
    $o4 = "x1FABCE00" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726163734_3460 {
  strings:
    $o0 = "dword_43B594" wide ascii nocase
    $o1 = "dword_43B20C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726163739_8786 {
  condition:
    auto_rule_20250726163731_2149 or auto_rule_20250726163734_3460
}