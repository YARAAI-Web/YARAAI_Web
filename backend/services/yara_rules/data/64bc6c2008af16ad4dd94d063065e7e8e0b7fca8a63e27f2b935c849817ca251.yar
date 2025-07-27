rule auto_rule_20250726202648_6429 {
  strings:
    $o0 = "_pFirstBlock" wide ascii nocase
    $o1 = "aInconsistentIo" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
    $o3 = "dword_4642C8" wide ascii nocase
    $o4 = "dword_464298" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726202651_1169 {
  strings:
    $o0 = "x12012u" wide ascii nocase
    $o1 = "xFEDu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726202654_9224 {
  condition:
    auto_rule_20250726202648_6429 or auto_rule_20250726202651_1169
}