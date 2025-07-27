rule auto_rule_20250726112312_4064 {
  strings:
    $o0 = "dword_42C739" wide ascii nocase
    $o1 = "dword_42C8A9" wide ascii nocase
    $o2 = "dword_42C701" wide ascii nocase
    $o3 = "x3658000098AELL" wide ascii nocase
    $o4 = "uIDNewItem" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726112315_0111 {
  strings:
    $o0 = "x2A23u" wide ascii nocase
    $o1 = "x8CCu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726112318_9771 {
  condition:
    auto_rule_20250726112312_4064 or auto_rule_20250726112315_0111
}