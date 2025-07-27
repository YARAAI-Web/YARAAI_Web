rule auto_rule_20250727000638_5855 {
  strings:
    $o0 = "stru_406060" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
    $o3 = "x402801" wide ascii nocase
    $o4 = "dword_407020" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727000641_2675 {
  strings:
    $o0 = "dword_449948" wide ascii nocase
    $o1 = "dword_407018" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727000645_4371 {
  condition:
    auto_rule_20250727000638_5855 or auto_rule_20250727000641_2675
}