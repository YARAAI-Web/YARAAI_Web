rule auto_rule_20250727034247_1977 {
  strings:
    $o0 = "_NLG_Notify" wide ascii nocase
    $o1 = "dword_476974" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "dword_475D88" wide ascii nocase
  condition:
    4 of ($o*)
}