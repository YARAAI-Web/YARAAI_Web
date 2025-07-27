rule auto_rule_20250726215813_8143 {
  strings:
    $o0 = "GetGuiResources" wide ascii nocase
    $o1 = "FlashWindow" wide ascii nocase
    $o2 = "iItem" wide ascii nocase
    $o3 = "GetKBCodePage" wide ascii nocase
    $o4 = "bRedraw" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215816_3893 {
  strings:
    $o0 = "lpClipRect" wide ascii nocase
    $o1 = "dword_41D9B4" wide ascii nocase
    $o2 = "lpwndpl" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726215820_0832 {
  condition:
    auto_rule_20250726215813_8143 or auto_rule_20250726215816_3893
}