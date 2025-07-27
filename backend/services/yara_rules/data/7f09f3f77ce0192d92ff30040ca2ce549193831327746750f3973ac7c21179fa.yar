rule auto_rule_20250726195424_3866 {
  strings:
    $o0 = "dword_43B1B8" wide ascii nocase
    $o1 = "dword_43B65C" wide ascii nocase
    $o2 = "E9762F1h" wide ascii nocase
    $o3 = "fnsave" wide ascii nocase
    $o4 = "dword_43B8CA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726195427_7113 {
  strings:
    $o0 = "x72D56700u" wide ascii nocase
    $o1 = "aQnpzuzufsqik" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726195431_8565 {
  condition:
    auto_rule_20250726195424_3866 or auto_rule_20250726195427_7113
}