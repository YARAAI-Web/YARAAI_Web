rule auto_rule_20250727012303_8301 {
  strings:
    $o0 = "dword_78100" wide ascii nocase
    $o1 = "dword_781A0" wide ascii nocase
    $o2 = "dword_1E544" wide ascii nocase
    $o3 = "word_1E74A" wide ascii nocase
  condition:
    4 of ($o*)
}