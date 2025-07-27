rule auto_rule_20250726105704_9779 {
  strings:
    $o0 = "dword_43B514" wide ascii nocase
    $o1 = "dword_43B898" wide ascii nocase
    $o2 = "dword_43B063" wide ascii nocase
    $o3 = "dword_43B56A" wide ascii nocase
    $o4 = "dword_43B020" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726105707_7775 {
  strings:
    $o0 = "dword_43B144" wide ascii nocase
    $o1 = "dword_43B6BD" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726105711_8085 {
  condition:
    auto_rule_20250726105704_9779 or auto_rule_20250726105707_7775
}