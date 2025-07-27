rule auto_rule_20250727042856_5820 {
  strings:
    $o0 = "dword_44C12C" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
    $o2 = "dword_44BEA0" wide ascii nocase
    $o3 = "off_44B554" wide ascii nocase
    $o4 = "old_esp" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727042859_0764 {
  strings:
    $o0 = "dword_44C28C" wide ascii nocase
    $o1 = "_global_unwind2" wide ascii nocase
    $o2 = "dword_44C4F8" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250727042903_4700 {
  condition:
    auto_rule_20250727042856_5820 or auto_rule_20250727042859_0764
}