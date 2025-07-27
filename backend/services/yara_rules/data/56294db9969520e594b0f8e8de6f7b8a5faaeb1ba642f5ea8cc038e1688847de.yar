rule auto_rule_20250726211951_9415 {
  strings:
    $o0 = "FlatSB_SetScrollRange" wide ascii nocase
    $o1 = "ldwTotsize" wide ascii nocase
    $o2 = "dwCreationDisposition" wide ascii nocase
    $o3 = "ppSecurityDescriptor" wide ascii nocase
    $o4 = "hDrop" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726211952_2087 {
  strings:
    $o0 = "StrRChrIA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726211957_1697 {
  condition:
    auto_rule_20250726211951_9415 or auto_rule_20250726211952_2087
}