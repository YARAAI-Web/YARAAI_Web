rule auto_rule_20250726144646_0273 {
  strings:
    $o0 = "x5572" wide ascii nocase
    $o1 = "dword_42E762" wide ascii nocase
    $o2 = "dword_412224" wide ascii nocase
    $o3 = "xFABF2DFF" wide ascii nocase
    $o4 = "x7510856u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726144649_9623 {
  strings:
    $o0 = "x42D20000001DLL" wide ascii nocase
    $o1 = "UsedDefaultChar" wide ascii nocase
    $o2 = "x2930" wide ascii nocase
    $o3 = "xF89C8530" wide ascii nocase
    $o4 = "xF89C8532" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726144652_0964 {
  condition:
    auto_rule_20250726144646_0273 or auto_rule_20250726144649_9623
}