from pydantic import BaseModel, Field


class Credentials(BaseModel):
    username: str
    password: str


class BaseMessage(BaseModel):
    class MailAccount(BaseModel):
        name: str
        address: str
    id: str

    accountId: str
    msgid: str
    from_: MailAccount = Field(alias="from")
    to: list[MailAccount]
    subject: str
    seen: bool
    isDeleted: bool
    hasAttachments: bool
    size: int
    downloadUrl: str
    createdAt: str
    updatedAt: str


class ShortMessage(BaseMessage):
    intro: str


class Message(ShortMessage):
    class Attachment(BaseModel):
        id: str
        filename: str
        contentType: str
        disposition: str
        transferEncoding: str
        related: bool
        size: int
        downloadUrl: str

    cc: list[str]
    bcc: list[str]
    flagged: bool
    verifications: list[str]
    retention: bool
    retentionDate: str
    text: str
    html: list[str]
    attachments: list[Attachment]
