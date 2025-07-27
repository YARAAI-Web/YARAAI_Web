rule auto_rule_20250726194244_6251 {
  strings:
    $o0 = "getsockopt" wide ascii nocase
    $o1 = "dword_43B577" wide ascii nocase
    $o2 = "aMzdiz" wide ascii nocase
    $o3 = "dword_43B7AD" wide ascii nocase
    $o4 = "aFilitomo" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726194248_0206 {
  strings:
    $o0 = "dword_43B4C4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726194253_9333 {
  condition:
    auto_rule_20250726194244_6251 or auto_rule_20250726194248_0206
}