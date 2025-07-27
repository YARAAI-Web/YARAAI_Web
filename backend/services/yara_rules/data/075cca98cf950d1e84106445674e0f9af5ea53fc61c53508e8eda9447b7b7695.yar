rule auto_rule_20250727004212_4107 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "dwInfoType" wide ascii nocase
    $o2 = "_ctype" wide ascii nocase
    $o3 = "dword_411E68" wide ascii nocase
    $o4 = "_NLG_Notify1" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727004215_8017 {
  strings:
    $o0 = "dword_40E01C" wide ascii nocase
    $o1 = "CPtoLCID" wide ascii nocase
    $o2 = "dword_411E64" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250727004227_3164 {
  condition:
    auto_rule_20250727004212_4107 or auto_rule_20250727004215_8017
}